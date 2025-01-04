from django.contrib import admin
from .models import SchoolAssignment
# from .models import ClassAssignment

@admin.register(SchoolAssignment)
class SchoolAssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'school', 'assigned_at')
    list_filter = ('school', 'student__gender', 'assigned_at')  # Filtrar por escuela, género del alumno y fecha
    search_fields = ('student__first_name', 'student__last_name', 'school__name')  # Búsqueda por nombres y escuela
    autocomplete_fields = ('school', 'student')  # Autocompletar para relaciones foráneas
    ordering = ('-assigned_at',)

    fieldsets = (
        ("Información de la Asignación", {
            'fields': ('school', 'student')
        }),
        ("Tiempos", {
            'fields': ('assigned_at',),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('assigned_at',)  # La fecha de asignación es solo de lectura
