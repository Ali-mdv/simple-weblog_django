from django.contrib import admin
from .models import Article, Category, IpAddress

from django.contrib import messages
from django.utils.translation import ngettext

# Actions

#@admin.action(description='انتشار مقالات انتخاب شده')
#def make_published(modeladmin, request, queryset):
#    queryset.update(status='p')

#@admin.action(description='پیش نوس کردن مقالات انتخاب شده')
#def make_drafted(modeladmin, request, queryset):
#    queryset.update(status='d')



# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','picture_tag','jpublish','category_to_str','author','status','is_special','hits_count')
    list_filter = ('title','slug','publish','status','is_special')
    search_fields = ('title','describtion')
    prepopulared_fields = {'slug':('title',)}
    ordeing = ['-status','-publish']
    actions = ['make_published','make_drafted']

    @admin.action(description='انتشار مقالات انتخاب شده')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d مقاله منتشر شد.',
            '%d مقاله منتشر شدند.',
            updated,
        ) % updated, messages.SUCCESS)


    @admin.action(description='پیش نویس مقالات انتخاب شده')
    def make_drafted(self, request, queryset):
        updated = queryset.update(status='d')
        self.message_user(request, ngettext(
            '%d مقاله پیش نویس شد.',
            '%d مقله پیش نویس  شدند.',
            updated,
        ) % updated, messages.SUCCESS)

admin.site.register(Article,ArticleAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent','slug','status')
    list_filter = ('title','slug','status')
    search_fields = ('title',)
    ordeing = ['position',]
    actions = ['make_active','make_inactive']

    @admin.action(description='نمایش دسته بندی')
    def make_active(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d دسته بندی فعال شد.',
            '%d دسته بندی عال شدند.',
            updated,
        ) % updated, messages.SUCCESS)


    @admin.action(description='عدم نمایش دسته بندی')
    def make_inactive(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d دسته بندی غیر فعال شد.',
            '%d دسته بندی غیر فعال شدند.',
            updated,
        ) % updated, messages.SUCCESS)

admin.site.register(Category,CategoryAdmin)




class IpAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    list_filter = ('ip_address',)
    search_fields = ('ip_address',)

admin.site.register(IpAddress,IpAddressAdmin)

