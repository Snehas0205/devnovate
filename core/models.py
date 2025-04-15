from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('SPONSOR', 'Sponsor'),
        ('PARTICIPANT', 'Participant'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='PARTICIPANT')
    company_name = models.CharField(max_length=200, blank=True, null=True)  # For Sponsors
    contact_info = models.CharField(max_length=200, blank=True, null=True)  # For Sponsors
    logo = models.ImageField(upload_to='sponsor_logos/', blank=True, null=True)  # For Sponsor Spotlight

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200, default="Hackathon 2025")
    date = models.DateTimeField(null=True, blank=True)
    is_virtual = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Sponsorship(models.Model):
    TIER_CHOICES = [
        ('GOLD', 'Gold ($5000)'),
        ('SILVER', 'Silver ($2500)'),
        ('BRONZE', 'Bronze ($1000)'),
    ]
    sponsor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tier = models.CharField(max_length=20, choices=TIER_CHOICES, default='BRONZE')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sponsor.user.username} - ${self.amount} ({self.tier})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
