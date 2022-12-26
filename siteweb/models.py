from django.db import models
import datetime
from .validators import validate_file_extension

# Create your models here.

class AppelOffre(models.Model):
    CATEGORIE = (
        ("services","Services"),
        ("travaux","Travaux"),
        ("fournitures","Fournitures"),
    )
    numero_AO = models.CharField(max_length=15, unique=True)
    date_publication = models.DateField(null=False, blank=False, default=datetime.date.today)
    categorie = models.CharField(max_length=15, choices=CATEGORIE, default='services')
    objet = models.CharField(max_length=100)
    lieu_execution = models.CharField(max_length=15)
    date_limite_remise = models.DateField(null=False, blank=False)
    date_ouverture = models.DateField(null=False, blank=False)
    avis_pdf = models.FileField(upload_to='ao/', default=None, validators=[validate_file_extension])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_archivage = models.DateField(null=False, blank=False)

    def serialize(self):
        return {
            "numero_AO": self.numero_AO,
            "categorie": self.categorie,
            "objet": self.objet,
            "date_limite_remise": self.date_limite_remise.strftime("%b %d %Y"),
            "pdf":self.avis_pdf.url,
        }
    def __str__(self):
        return self.numero_AO

class Recrutement(models.Model):
    CONTRAT = (
        ("cdd","CDD"),
        ("cdi","CDI"),
    )
    date_publication = models.DateField(null=False, blank=False, default=datetime.date.today)
    date_limite_candidature = models.DateField(null=False, blank=False)
    date_concours = models.DateField(null=False, blank=False)
    fonction = models.CharField(max_length=15)
    type_contrat = models.CharField(max_length=15, choices=CONTRAT, default='cdd')
    nombre_poste = models.PositiveIntegerField(default=10)
    avis_pdf = models.FileField(upload_to='recrutement/', default=None, validators=[validate_file_extension])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_archivage = models.DateField(null=False, blank=False)

    def serialize(self):
        return {
            "fonction": self.fonction,
            "nombre_poste": self.nombre_poste,
            "type_contrat": self.type_contrat,
            "date_limite_candidature": self.date_limite_candidature.strftime("%b %d %Y"),
            "pdf":self.avis_pdf.url,
        }

    def __str__(self):
        return self.fonction + " --- contrat "+self.type_contrat