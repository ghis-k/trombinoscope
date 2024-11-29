from django.contrib import admin
from .models import Personne,Formation,Competence,Experience
class adminpersonne(admin.ModelAdmin):
    actions = ['delete_selected']
    list_display=('photo','nom','prenom','telephone','mail','actif' )
# Register your models here.
admin.site.register(Personne,adminpersonne)
admin.site.register(Formation)
admin.site.register(Competence) 
admin.site.register(Experience) 
