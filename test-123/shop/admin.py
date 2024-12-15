from django.contrib import admin
from shop.models import Category, Item, Tag

# Register your models here.
# class ItemInline(admin.TabularInline):
#     model = Item
#     extra = 1

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1

class TagItemInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class TagInline(admin.StackedInline):
    model = Tag.items.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']
    ordering = ['name','id']
    list_per_page = 10
    inlines = [ItemInline]


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']
    ordering = ['price']
    autocomplete_fields = ['category'] 
    fields = ['name','category', 'price','description', ]
    inlines = [TagInline]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    autocomplete_fields = ['items']
    inlines = [TagItemInline] 

admin.site.register(Tag, TagAdmin)

admin.site.register(Item, ItemAdmin)

admin.site.register(Category, CategoryAdmin)