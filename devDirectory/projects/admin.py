from django.contrib import admin

# Register your models here.
from .models import Project,Review,Tag,Post

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Post)
