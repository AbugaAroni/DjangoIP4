from django.contrib import admin
from .models import user, neighbourhood, business, post
# Register your models here.

admin.site.register(user)
admin.site.register(neighbourhood)
admin.site.register(business)
admin.site.register(post)
