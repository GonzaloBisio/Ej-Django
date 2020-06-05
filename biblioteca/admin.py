from django.contrib import admin

from .models import *
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Usuario)