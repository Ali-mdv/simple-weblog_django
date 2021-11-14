from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from user.models import User
from user.mixins import AuthorAccessMixin

from django.db.models import Q

# Create your views here.


def home(request,page=1):
   # return HttpResponse('<h4>Django</h4><hr>')
    articles = Article.objects.published()
    paginator = Paginator(articles,1)
    page_obj = paginator.get_page(page)
    context = {
        #'articles':Article.objects.all(),
        'articles':page_obj,
        }
    return render(request,'article/home.html',context)


class Home(ListView):
    # model = Article 
    queryset = Article.objects.published()
    # template_name = 'article/home.html' # => defualt template name is article_list
    # context_object_name = 'articles' # => defualt context name is object_list
    paginate_by = 10

#====================================================================================

def detail(request,slug):
    article = get_object_or_404(Article,slug=slug,status='p')
    context = {
            'article':article,
            }
    return render(request,'article/detail.html',context)


class Detail(DetailView):
    template_name = 'article/article_detail.html' # => defualt template name is object_list
    # context_object_name = 'article' # => defualt context name is object
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(),slug=slug)
        ip_address = self.request.user.ip_address

        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
            
        return article


#====================================================================================

class Preview(AuthorAccessMixin,DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article,pk=pk)

#====================================================================================

def category(request,slug,page=1):
    category = get_object_or_404(Category.objects.active(),slug=slug)
    articles = category.articles.published()
    paginator = Paginator(articles,1)
    page_obj = paginator.get_page(page)
    context = {
            'category':category,
            'articles':page_obj,
            }
    return render(request,'article/category.html',context)

class CategoryView(ListView):
    template_name = 'article/category.html'
    paginate_by = 10

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(),slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

#===========================================================================

class AuthorView(ListView):
    template_name = 'article/author.html'
    paginate_by = 10

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context

#===========================================================================

class SearchList(ListView):
    template_name = 'article/searchـlist.html'
    paginate_by = 6

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(title__icontains=search) | Q(describtion__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
