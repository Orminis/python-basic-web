from django.db import models


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
    code_name = models.CharField(max_length=30, unique=True)
    deadline = models.DateField()


class Employee(AuditInfoMixin):
    """
    Employee.objects.all()      # Select *
    Employee.objects.create()   # Insert
    Employee.objects.filter()   # Select + Where
    Employee.objects.update()   # Update
    Employee.objects.raw()      # raw SQL
    etc...
    """

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
    # int > 0
    years_of_exp = models.PositiveIntegerField()
    # Text
    review = models.TextField()
    # Char field with included validator for emails
    email = models.EmailField()
    # Boolean field (True/False)
    works_full_time = models.BooleanField()
    photo = models.URLField()
    # Date field
    start_date = models.DateField()
    # Date/Time field
    birth_date = models.DateField()

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

    # one-to-many relations
    department = models.ForeignKey(
        to=Department,
        # when the department is deleted all employees will be deleted too
        on_delete=models.CASCADE,
        default=0
        # set null: department field for the specific employee will be set to null when his/her department is deleted
        # on_delete=models.SET_NULL,
        # null=True
        # Restrict: if any employee is associated to department X, X can not be deleted because some employee is associated to it.
        # on_delete=models.RESTRICT,
    )

    # many-to-many relations        # model to relate,
    projects = models.ManyToManyField(Project)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # return f"ID: {self.pk}; Name: {self.first_name} {self.last_name}"
        return f"ID: {self.pk}; Name: {self.fullname}"


# diff between null and blank
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
