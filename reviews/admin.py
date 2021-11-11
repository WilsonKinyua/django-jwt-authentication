from django.contrib import admin
from .models import Product, Category, Company, ProductSize, ProductSite, Comment
from django.contrib.auth.models import Group


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)


# unregister models
admin.site.unregister(Group)


# change the title of the admin page
admin.site.site_header = 'Product Reviews Admin'