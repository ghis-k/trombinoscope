from django.db import models


# Create your models here.
class Personne(models.Model):
    nom=models.CharField(max_length=150)
    
    prenom=models.CharField(max_length=150)
    telephone=models.CharField(max_length=10)
    mail=models.EmailField()
    photo=models.ImageField(upload_to='image/', null=True, blank=True)
    
    #prenom=models.CharField(null=True)
    # c'est un exemple d'insertion de champ 
    #(null=True) pour dir que les ceux qui etait dans la table auron un valeur null
    actif=models.BooleanField(default=True)#pour augmenter librement un champ
    def __str__(self):
        return f'{self.nom}'

class Experience(models.Model):
    personne = models.ForeignKey(Personne, related_name='experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.job_title} chez {self.company_name}'

class Formation(models.Model):
    personne = models.ForeignKey(Personne, related_name='formations', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.degree} à {self.school_name}'

class Competence(models.Model):
    personne = models.ForeignKey(Personne, related_name='competences', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    level = models.IntegerField()  # Par exemple : de 1 à 100 %

    def __str__(self):
        return self.skill_name
# chaque foi que vous modifiez ma table ou ma classe du model 
#voici les deux les deux commendes
#python manage.py makemigrations
#python manage.py migrate
  
   