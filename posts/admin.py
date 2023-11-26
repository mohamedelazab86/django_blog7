from django.contrib import admin
from .models import Post,Category,Comments
from django_summernote.admin import SummernoteModelAdmin


# customize on admin panel
class PostAdmin(SummernoteModelAdmin):
    list_display=['title','draft']
    list_filter=['title']
    search_fields=['title']
    summernote_fields = ('content',)



# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comments)
