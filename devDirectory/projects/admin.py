from django.contrib import admin

# Register your models here.
from .models import Project,Review,Tag,Post,LikePost,Jobs

admin.site.register(Project)
admin.site.register(Jobs)
admin.site.register(LikePost)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Post)
