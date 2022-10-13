from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Centre(models.Model):
    nom = models.CharField(max_length=150,unique=True)
    adress = models.CharField(max_length=150)
    number = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True,unique=True)


    def __str__(self):
        return self.nom
    
class Salle(models.Model):
    number = models.IntegerField()
    capacite = models.IntegerField()
    centre=models.ForeignKey(Centre, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number )+str(self.centre)
    


class Formateur(models.Model):
    nom = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    numero = models.CharField(max_length=150)
    salaire = models.FloatField()
    formateur_number = models.IntegerField( primary_key=True)
    email = models.EmailField(max_length=70,unique=True)
    gender_choice = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)    

    def __str__(self):
        return self.nom



    
class Formation(models.Model):
    nom = models.CharField(max_length=150, primary_key=True)
    prix = models.FloatField()
    category = models.CharField(max_length=100)
    date_debut = models.DateField
    date_fin = models.DateField
    Formateur = models.ForeignKey(Formateur, on_delete=models.DO_NOTHING)
    salle=models.OneToOneField(Salle,default=1,
                 on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.nom



    
class Etudiant(models.Model):
    academic_year = models.DateField
    formation = models.ManyToManyField(Formation)
    nom = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    number = models.IntegerField()
    student_number = models.IntegerField( primary_key=True)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    gender_choice = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)    
    isvalidated = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nom
    
    




class Review(models.Model):
    body = models.CharField(max_length=100)
    reviewer=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    isvalidated = models.BooleanField(default=False)

    def __str__(self):
        return self.body
