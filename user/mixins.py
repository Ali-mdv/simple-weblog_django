from django.http import Http404
from article.models import Article
from django.shortcuts import get_object_or_404, redirect


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ('author','title','slug','category','describtion','picture','publish','status','is_special','video')
        elif request.user.is_author:
            self.fields = ('title','slug','category','describtion','picture','publish','is_special','status','video')
        else:
            raise Http404('شما دسترسی به این صفحه ندارید')

        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if self.obj.status != 'i':
                self.obj.status = 'd'

        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if article.status=='d' or 'b' and article.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما دسترسی به این صفحه ندارید')

        

class SuperAccessUserMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('شما دسترسی به این صفحه ندارید')



class AuthorsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')
