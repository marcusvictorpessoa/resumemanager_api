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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.PositiveBigIntegerField(unique=True)
    experience_area = models.CharField(max_length=255)
    resume = models.FileField(upload_to='pdf')
    resume_avaliation = models.CharField(max_length=9, choices=Avaliation.choices, default=Avaliation.REGULAR)
    note = models.TextField()

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['created_at']


    def __str__(self):
        return self.name