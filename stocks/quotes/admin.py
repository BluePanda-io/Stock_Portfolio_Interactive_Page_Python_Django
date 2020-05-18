from django.contrib import admin
from .models import Stock # from the file models we import the class stock

admin.site.register(Stock) # and then we finally have to resigter this to the admin page 

