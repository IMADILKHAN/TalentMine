from django.contrib import admin

# Register your models here.
from .models import Project,Review,Tag,Jobs

admin.site.register(Project)
admin.site.register(Jobs)
admin.site.register(Review)
admin.site.register(Tag)
