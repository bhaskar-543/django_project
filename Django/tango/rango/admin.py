from django.contrib import admin
from rango.models import UserProfile
#from rango.models import category,Page
# Register your models here.
from rango.models import Category, Page
#admin.site.register(Category)
#admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category','url')
admin.site.register(Page,PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
