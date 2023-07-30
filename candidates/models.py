from django.db import models
import uuid
# Create your models here.

class Base(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Candidate(Base):

    class Avaliation(models.TextChoices):
        REGULAR = 'regular'
        BOM =  'bom'
        OTIMO = 'ótimo'
        EXCELENTE = 'excelente'

    class ProcessResults(models.TextChoices):
        EM_ESPERA = 'em espera'
        APROVADO = 'aprovado'
        REPROVADO = 'reprovado'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.PositiveBigIntegerField(unique=True)
    experience_area = models.CharField(max_length=255)
    resume = models.FileField(upload_to='pdf')
    resume_avaliation = models.CharField(max_length=9, choices=Avaliation.choices, default=Avaliation.REGULAR)
    selective_process = models.CharField(max_length=255)
    result = models.CharField(max_length=9, choices=ProcessResults.choices, default=ProcessResults.EM_ESPERA)
    note = models.TextField()

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['created_at']


    def __str__(self):
        return self.name