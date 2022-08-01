from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    form = PostAdminForm
    save_as = True
    list_display = ('id','title','slug','category','get_photo')

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src-"{obj.photo.url}" width-"50">')
        return '-'

    get_photo.short_description = 'фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
