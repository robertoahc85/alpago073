from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings

class School(models.Model):
    INSTITUTION_TYPES = (
        ('publica', 'Pública'),
        ('privada', 'Privada'),
        ('subsidiada', 'Subsidiada'),
    )
    
    EDUCATION_LEVELS = (
        ('preescolar', 'Preescolar'),
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('media_superior', 'Media Superior'),
        ('superior', 'Superior'),
    )
    
    EDUCATION_MODALITIES = (
        ('escolarizada', 'Escolarizada'),
        ('no_escolarizada', 'No Escolarizada'),
        ('mixta', 'Mixta'),
    )
    
    SHIFTS = (
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('nocturno', 'Nocturno'),
        ('tiempo_completo', 'Tiempo Completo'),
    )
     # Opciones para Estados de México
    MEXICO_STATES = [
        ('AG', 'Aguascalientes'),
        ('BC', 'Baja California'),
        ('BS', 'Baja California Sur'),
        ('CH', 'Chihuahua'),
        ('CL', 'Colima'),
        ('CM', 'Campeche'),
        ('CO', 'Coahuila'),
        ('CS', 'Chiapas'),
        ('DF', 'Ciudad de México'),
        ('DG', 'Durango'),
        ('GT', 'Guanajuato'),
        ('GR', 'Guerrero'),
        ('HG', 'Hidalgo'),
        ('JA', 'Jalisco'),
        ('MX', 'Estado de México'),
        ('MI', 'Michoacán'),
        ('MO', 'Morelos'),
        ('NA', 'Nayarit'),
        ('NL', 'Nuevo León'),
        ('OA', 'Oaxaca'),
        ('PU', 'Puebla'),
        ('QE', 'Querétaro'),
        ('QR', 'Quintana Roo'),
        ('SI', 'Sinaloa'),
        ('SL', 'San Luis Potosí'),
        ('SO', 'Sonora'),
        ('TB', 'Tabasco'),
        ('TL', 'Tlaxcala'),
        ('TM', 'Tamaulipas'),
        ('VE', 'Veracruz'),
        ('YU', 'Yucatán'),
        ('ZA', 'Zacatecas'),
    ]


    name = models.CharField('Nombre', max_length=200)
    institution_type = MultiSelectField(
        'Tipo de Institución',
        choices=INSTITUTION_TYPES,
        max_length=100
    )
    education_level = MultiSelectField(
        'Nivel Educativo',
        choices=EDUCATION_LEVELS,
        max_length=100
    )
    education_modality = MultiSelectField(
        'Modalidad Educativa',
        choices=EDUCATION_MODALITIES,
        max_length=100
    )
    shifts = MultiSelectField(
        'Turnos',
        choices=SHIFTS,
        max_length=100
    )
    street = models.CharField('Calle', max_length=200)
    number = models.CharField('Número', max_length=20)
    neighborhood = models.CharField('Colonia', max_length=200)
    municipality = models.CharField('Municipio', max_length=200)
    state = models.CharField(
        max_length=2,
        choices=MEXICO_STATES,
        verbose_name="Estado"
    )
    postal_code = models.CharField('Código Postal', max_length=10)
    phone = models.CharField('Teléfono', max_length=20)
    email = models.EmailField('Correo Electrónico', max_length=254)
    website = models.URLField('Sitio Web', blank=True, null=True)
    logo = models.ImageField('Logotipo', upload_to='school_logos/', blank=True, null=True)
    active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de Actualización', auto_now=True)
    
    # Cambiar la relación ManyToManyField
    students = models.ManyToManyField('students.Student', blank=True, related_name='schools')

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'

    def __str__(self):
        return self.name