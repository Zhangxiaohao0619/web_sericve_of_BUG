#coding=utf-8
from django.contrib import admin
from .models import Article,Person


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
    #筛选
    search_fields = ('title',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    search_fields = ('first_name',)
    #列表
    list_filter = ('first_name',)

    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super().get_search_results(request, queryset, search_term)
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset |= self.model.objects.filter(age=search_term_as_int)
    #     return queryset, use_distinct

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)

# Register your models here.
