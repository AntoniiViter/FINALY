from django.contrib import admin
from .models import News, Comments


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(News, NewsAdmin)


admin.site.register(Comments, CommentsAdmin)