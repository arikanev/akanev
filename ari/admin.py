from django.contrib import admin
from .models import Page
from .models import Email
from .models import URL
from .models import Image
from .models import Summary

# Register your models here.
admin.site.register(Page)
admin.site.register(Email)
admin.site.register(URL)
admin.site.register(Image)
admin.site.register(Summary)
