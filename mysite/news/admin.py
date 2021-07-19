from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from weather.models import City


class NewsAdminForm(forms.ModelForm):    # Визуальный редактор CKEditor 49
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'update_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'update_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return ' -- '

    get_photo.short_description = 'Фото' # кастомизация админки 41
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Управление новостями'
admin.site.site_title = 'Управление новостями'



admin.site.register(City)


