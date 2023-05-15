from django.db import models

"""
Django ORM (Object-relational mapping).
"""
# Create your models here.
from django.urls import reverse


class AuditInfoMixin(models.Model):
    class Meta:
        # No table will be created in the DB!!!
        # Can be inherited in other models
        abstract = True

    # Automatically filled upon creation of an object in corresponding child class table
    created_on = models.DateTimeField(auto_now=True)
    # Automatically filled on any update of an object in corresponding child class table
    updated_on = models.DateTimeField(auto_now_add=True)


class Department(AuditInfoMixin):
    name = models.CharField(max_length=20)
    slug = models.SlugField(
        unique=True,
        # null=True, само за 1вата миграция ако има данни в дб и искаме да направим миграциятая3
    )

    def __str__(self):
        # return f"ID: {self.pk}; Name: {self.first_name} {self.last_name}"
        return f"ID: {self.pk}; Name: {self.name}"

    # method which returns the url to give you information for the object
    def get_absolute_url(self):
        url = reverse("details department", kwargs={"pk": self.pk, "slug": self.slug, })
        return url


class Project(AuditInfoMixin):
    name = models.CharField(max_length=45)
    code_name = models.CharField(
        max_length=30,
        unique=True
    )
    deadline = models.DateField()

# Class inheriting Enum for specific enum choices.
# https://stackoverflow.com/questions/54802616/how-can-one-use-enums-as-a-choice-field-in-a-django-model
# class EmployeeLevel(Enum):
#     LEVEL_JUNIOR = "Junior"
#     LEVEL_REGULAR = "Regular"
#     LEVEL_SENIOR = "Senior"


class Employee(AuditInfoMixin):
    """
    Employee.objects.all()      # Select *
    Employee.objects.create()   # Insert
    Employee.objects.filter()   # Select + Where
    Employee.objects.update()   # Update
    Employee.objects.raw()      # raw SQL
    etc...
    """
    #
    class Meta:
        ordering = ("years_of_exp", '-birth_date')

    LEVEL_JUNIOR = "Junior"
    LEVEL_REGULAR = "Regular"
    LEVEL_SENIOR = "Senior"

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    # int >= 0
    years_of_exp = models.PositiveIntegerField()
    # Text
    review = models.TextField()
    # Char field with included validator for emails
    email = models.EmailField(
        unique=True,
    )
    # Boolean field (True/False)
    works_full_time = models.BooleanField()
    photo = models.URLField()
    # Date field
    start_date = models.DateField()
    # Date/Time field
    birth_date = models.DateTimeField()

    # Can be put in abstract class so every child class to have the same columns.
    # # Automatically filled upon creation of an Employee
    # created_on = models.DateTimeField(auto_now=True)
    # # Automatically filled on any update of the specific employee
    # updated_on = models.DateTimeField(auto_now_add=True)

    # choices
    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        # changes from level to Seniority Level in the admin panel. only for visualization
        verbose_name="Seniority Level"
    )


# on_delete has 3 options:
# * on_delete=models.CASCADE :
# When the department is deleted all employees will be deleted too.
# It means all linked rows in the class Employees to the row from Department will be deleted.
#
# * on_delete=models.SET_NULL, null=True :
# Set null: department field for the specific employee will be set to null when his/her department is deleted. It must
# be accompanied by set=null.
#
# * on_delete=models.RESTRICT :
# Restrict: if any employee is associated to department X, X can't be deleted because an employee is associated to it.

    # one-to-many relations
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

    # many-to-many relations
    # model to relate
    projects = models.ManyToManyField(Project)

    # second way to make many-to-many relations is with option through. In this case we need to make a new junction table
    # manually which to be used for the relations between the tables. 
    # projects = models.ManyToManyField(
    #     Project,
    #     related_name='employees',
    #     through='EmployeesProjects'
    # )
    # property is not reflected in the DB
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # return f"ID: {self.pk}; Name: {self.first_name} {self.last_name}"
        return f"ID: {self.pk}; Name: {self.fullname}"


# diff between null and blank, blank is used for form validation, null is for db validation.
class NullBlankDemo(models.Model):
    # blank = models.IntegerField(
    #     blank=True,
    #     null=False,
    # )
    # null = models.IntegerField(
    #     blank=False,
    #     null=True,
    # )
    blanknull = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )


# custom junction table for Many to Many relationship.
class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)
    # additional info
    date_joined = models.DateField(

    )
    # after that includes through option in the main


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )



class Category(models.Model):
    category = models.CharField(
        max_length=15,
    )

    # parent_category = models.ForeignKey(
    #     "apps.models_03.models.Category",
    #     on_delete=models.CASCADE,
    # )