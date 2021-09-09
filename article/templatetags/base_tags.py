from django import template
from ..models import Category, Article

from django.db.models import Count, Q ,Avg
from datetime import datetime ,timedelta


register = template.Library()

@register.simple_tag
def title():
    return 'وبلاگ کریپتو'



@register.inclusion_tag('article/template_tags/category_tags.html')
def category_navbar():
    return {
        'category':Category.objects.active(),
        }


@register.inclusion_tag('registration/template_tags/link.html')
def link(request,link_name,icon,content):
    return {
        'request':request,
        'link_name' : link_name,
        'link': f'account:{link_name}',
        'icon':icon,
        'content':content,
    }


@register.inclusion_tag('article/template_tags/popular_articles.html')
def popular_articles():
    last_month = datetime.today() - timedelta(30)
    articles = Article.objects.published().annotate(
        count=Count('hits',filter=Q(articlehits__created__gt=last_month))
        ).order_by('-count','-publish')[:4]

    return{
        'articles':articles,
    }


@register.inclusion_tag('article/template_tags/hot_articles.html')
def hot_articles():
    last_month = datetime.today() - timedelta(30)
    articles = Article.objects.published().annotate(
        count=Count('comments',filter=Q(comments__posted__gt=last_month) & Q(comments__content_type_id=7))
        ).order_by('-count','-publish')[:4]


    return {
        'articles':articles,
    }



@register.inclusion_tag('article/template_tags/top_articles.html')
def top_articles():
    articles = Article.objects.published().annotate(
        avg_rating=Avg('ratings__average',filter=Q(ratings__content_type_id=7))
        ).order_by('-avg_rating')[:4]
    return {
        'articles':articles,
    }




@register.inclusion_tag('article/template_tags/popular-top-hot_articles.html')
def best_articles():
    last_month = datetime.today() - timedelta(30)
    
    return {
        'popular_article':Article.objects.published().annotate(
        count=Count('hits',filter=Q(articlehits__created__gt=last_month))
        ).order_by('-count','-publish')[0:1],
        'top_article':Article.objects.published().annotate(
        count=Count('comments',filter=Q(comments__posted__gt=last_month) & Q(comments__content_type_id=7))
        ).order_by('-count','-publish')[0:1],
        'hot_article':Article.objects.published().annotate(
        avg_rating=Avg('ratings__average',filter=Q(ratings__content_type_id=7))
        ).order_by('-avg_rating')[0:1],
    }




@register.inclusion_tag('article/template_tags/top_categories.html')
def top_categories():
    categories = Category.objects.active().annotate(
        count=Count('articles__hits')).order_by('-count')[:5]
    return {
        'categories':categories
    }
