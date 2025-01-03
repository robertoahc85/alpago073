from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No especificado'),
    ]

    first_name = models.CharField(max_length=255, verbose_name="Nombre")
    last_name = models.CharField(max_length=255, verbose_name="Apellido paterno")
    middle_name = models.CharField(max_length=255, verbose_name="Apellido materno", null=True, blank=True)
    birth_date = models.DateField(verbose_name="Fecha de nacimiento (DD/MM/AAAA)")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Género")
    curp = models.CharField(max_length=18, unique=True, verbose_name="CURP")
    enrollment_number = models.CharField(max_length=20, unique=True, verbose_name="Número de matrícula")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name or ''}"
