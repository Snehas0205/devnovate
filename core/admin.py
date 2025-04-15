from django.contrib import admin
from .models import Profile, Team, Event, Sponsorship, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'company_name', 'contact_info')  # Include relevant fields
    search_fields = ('user__username', 'role', 'company_name', 'contact_info')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_virtual')
    search_fields = ('name',)

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'event', 'amount', 'tier', 'created_at')
    search_fields = ('sponsor__user__username', 'tier')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'created_at')
    search_fields = ('title', 'team__name')
