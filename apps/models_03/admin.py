from django.contrib import admin

from apps.models_03.models import Employee, Project, Department


# Register your models here.

# The `Employee` model is enabled in django admin.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level', 'department')
    list_filter = ('level', 'department')
    search_fields = ('first_name', 'last_name')
    # fields = [('first_name', 'last_name'), 'level']
    fieldsets = (
        (
            'Personal Info',
            {
             'fields': ('first_name', 'last_name', 'age',)
            }
         ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_exp',)
            }
        ),
        (
            'Company Info',
            {
                'fields': ('department', 'is_full_time',)
            }
        ),
    )

    def department_name(self, obj):
        return obj.department.name


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
