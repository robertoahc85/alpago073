from django.db import models
from school.models import School
from students.models import Student
# from classes.models import Class

class SchoolAssignment(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="Escuela")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Alumno")
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de asignación")

    class Meta:
        unique_together = ('school', 'student')  # Un alumno solo puede asignarse una vez a la misma escuela
        verbose_name = "Asignación de Escuela"
        verbose_name_plural = "Asignaciones de Escuelas"

    def __str__(self):
        return f"{self.student} asignado a {self.school}"
