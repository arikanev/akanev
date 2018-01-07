from django.contrib import admin
from .models import User
from .models import Email
from .models import URL
from .models import Image
from .models import Bio
from .models import User_ID

# Register your models here.
admin.site.register(User)
admin.site.register(Email)
admin.site.register(URL)
admin.site.register(Image)
admin.site.register(Bio)
admin.site.register(User_ID)
