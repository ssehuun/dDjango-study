from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Person

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'modify_date')
	list_filter = ('modify_date',)
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug': ('title',)}

class PersonAdmin (admin.ModelAdmin):
	pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Post, PostAdmin)

