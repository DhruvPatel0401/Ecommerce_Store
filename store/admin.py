# from django.contrib import admin

# from .models import Category, Product


# # Registers model to admin panel
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug"]  # Displays fields in list view in admin panel from model
#     prepopulated_fields = {"slug": ("name",)}  # Automatically generates slug from name field


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["title", "author", "slug", "price", "in_stock", "created", "updated"]
#     list_filter = ["in_stock", "is_active"]  # Add filters to the right sidebar of the list view
#     list_editable = ["price", "in_stock"]  # Allows editing directly in list view
#     prepopulated_fields = {"slug": ("title",)}
