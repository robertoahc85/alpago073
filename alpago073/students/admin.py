from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'enrollment_number', 'gender', 'birth_date', 'curp')
    list_filter = ('gender', 'birth_date')
    search_fields = ('first_name', 'last_name', 'middle_name', 'curp', 'enrollment_number')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ("Información Personal", {
            'fields': ('first_name', 'last_name', 'middle_name', 'birth_date', 'gender')
        }),
        ("Identificación", {
            'fields': ('curp', 'enrollment_number')
        }),
        ("Tiempos", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Opcional: colapsar esta sección
        }),
    )
