from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.html import format_html
from .models import School  # Cambia 'school' por 'School'
from students.models import Student
from .forms import SchoolAdminForm


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    form = SchoolAdminForm
    list_display = (
        'name', 'get_institution_type', 'get_education_level',
        'get_education_modality', 'get_shifts', 'phone', 'email',
        'logo_preview', 'active', 'created_at'
    )
    list_filter = ('institution_type', 'education_level', 'education_modality', 'shifts', 'active', 'state')
    search_fields = ('name', 'email', 'phone', 'street', 'neighborhood', 'municipality', 'state', 'postal_code')
    readonly_fields = ('created_at', 'updated_at', 'logo_preview')
    ordering = ('-created_at',)

    fieldsets = (
        ("Información General", {
            'fields': ('name', 'institution_type', 'education_level', 'education_modality', 'shifts', 'active')
        }),
        ("Dirección", {
            'fields': ('street', 'number', 'neighborhood', 'municipality', 'state', 'postal_code')
        }),
        ("Contacto", {
            'fields': ('phone', 'email', 'website')
        }),
        ("Logotipo", {
            'fields': ('logo', 'logo_preview')
        }),
        ("Tiempos", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    actions = ['mark_as_active', 'mark_as_inactive', 'assign_students']

    # Métodos personalizados para multiselección
    def get_institution_type(self, obj):
        return ", ".join(obj.institution_type)
    get_institution_type.short_description = "Tipo de institución"

    def get_education_level(self, obj):
        return ", ".join(obj.education_level)
    get_education_level.short_description = "Nivel educativo"

    def get_education_modality(self, obj):
        return ", ".join(obj.education_modality)
    get_education_modality.short_description = "Modalidad educativa"

    def get_shifts(self, obj):
        return ", ".join(obj.shifts)
    get_shifts.short_description = "Turnos"

    # Vista previa del logotipo
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.logo.url)
        return "Sin logotipo"
    logo_preview.short_description = "Vista previa del logotipo"

    # Acciones personalizadas
    def mark_as_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, f"{updated} escuela(s) marcadas como activas.")
    mark_as_active.short_description = "Marcar como activas"

    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, f"{updated} escuela(s) marcadas como inactivas.")
    mark_as_inactive.short_description = "Marcar como inactivas"

    # Acción personalizada: Asignar alumnos a escuelas
    def assign_students(self, request, queryset):
        if 'apply' in request.POST:
            selected_students = request.POST.getlist('students')
            for school in queryset:
                for student_id in selected_students:
                    student = Student.objects.get(pk=student_id)
                    school.students.add(student)
            self.message_user(request, f"Alumnos asignados exitosamente a {queryset.count()} escuela(s).")
            return

        students = Student.objects.all()
        return render(request, 'admin/assign_students.html', {
            'students': students,
            'schools': queryset,
        })

    assign_students.short_description = "Asignar alumnos a escuelas"

    # URLs personalizadas
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('assign-students/', self.admin_site.admin_view(self.assign_students), name="assign-students"),
        ]
        return custom_urls + urls
