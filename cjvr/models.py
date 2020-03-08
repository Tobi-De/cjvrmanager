from django.contrib.auth.models import User
from django.db import models


class AggressionType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Victim(models.Model):
    SEX_COICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unsure'))
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=6, choices=SEX_COICES)
    address = models.CharField(max_length=60, blank=False)
    religion = models.CharField(max_length=30)
    register_date = models.DateTimeField(auto_now_add=True)
    VICTIM_STATUS = (('Alive', 'Alive'), ('Death', 'Death'),
                     ('Unknown', 'Unknown'))
    aggression_place = models.CharField(max_length=60, blank=False)
    status = models.CharField(max_length=10, choices=VICTIM_STATUS)
    aggressions = models.ManyToManyField(AggressionType)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name', 'age'], name='unique person')
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Plaintiff(models.Model):
    SEX_COICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unsure'))
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=6, choices=SEX_COICES)
    address = models.CharField(max_length=60, blank=False)
    religion = models.CharField(max_length=30)
    register_date = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=15, blank=False, unique=True, error_messages={
        'unique': "Un plaignant possedant ce contact est deja enregistrer."
    }, )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Testimony(models.Model):
    plaintiff = models.ForeignKey(Plaintiff, on_delete=models.CASCADE)
    victim = models.ForeignKey(Victim, on_delete=models.CASCADE)
    description = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['plaintiff', 'victim'], name='unique testimony')
        ]

    def __str__(self):
        return f"Deposition No{self.id}"


class Report(models.Model):
    testimony = models.OneToOneField(Testimony, on_delete=models.CASCADE)
    content = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
