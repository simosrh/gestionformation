from django.contrib import admin

# Register your models here.
from .models import Etudiant, Formateur, Review, Formation, Salle, Centre

admin.site.register(Etudiant)
admin.site.register(Formateur)
admin.site.register(Review)
admin.site.register(Formation)
admin.site.register(Salle)
admin.site.register(Centre)