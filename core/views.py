from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'profile'):
            login(request, user)
            if user.profile.role == 'ADMIN':
                return redirect('admin_dashboard')
            elif user.profile.role == 'SPONSOR':
                return redirect('sponsor_front')
            else:
                return redirect('participant_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    role = request.GET.get('role', 'PARTICIPANT')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = Profile.objects.create(user=user, role=role)
            login(request, user)
            if role == 'ADMIN':
                return redirect('admin_dashboard')
            elif role == 'SPONSOR':
                return redirect('sponsor_front')
            else:
                return redirect('participant_dashboard')
        else:
            messages.error(request, 'Error in form submission. Please try again.')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm(initial={'role': role})
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'role': role
    })

@login_required
def admin_dashboard(request):
    participants = Profile.objects.filter(role='PARTICIPANT')
    sponsors = Profile.objects.filter(role='SPONSOR')
    return render(request, 'admin_dashboard.html', {
        'profiles': participants,
        'sponsors': sponsors,
        'role': 'ADMIN'
    })

@login_required
def sponsor_front(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'SPONSOR':
        return redirect('index')
    from .models import Sponsorship, Project, Event
    from .forms import SponsorshipForm, SponsorProfileForm
    sponsorships = Sponsorship.objects.filter(sponsor=request.user.profile)
    projects = Project.objects.all()
    events = Event.objects.all()
    events_count = events.count()
    projects_count = projects.count()
    sponsorship_form = SponsorshipForm()
    profile_form = SponsorProfileForm(instance=request.user.profile)
    return render(request, 'sponsor_front.html', {
        'sponsorships': sponsorships,
        'projects': projects,
        'events': events,
        'events_count': events_count,
        'projects_count': projects_count,
        'sponsorship_form': sponsorship_form,
        'profile_form': profile_form,
        'role': 'SPONSOR'
    })

@login_required
def create_sponsorship(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'SPONSOR':
        return redirect('index')
    from .models import Sponsorship
    from .forms import SponsorshipForm
    if request.method == 'POST':
        form = SponsorshipForm(request.POST)
        if form.is_valid():
            sponsorship = form.save(commit=False)
            sponsorship.sponsor = request.user.profile
            sponsorship.save()
            messages.success(request, 'Sponsorship created successfully!')
            return redirect('sponsor_front')
        else:
            messages.error(request, 'Error creating sponsorship. Please check the form.')
    return redirect('sponsor_front')

@login_required
def update_sponsor_profile(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'SPONSOR':
        return redirect('index')
    from .forms import SponsorProfileForm
    if request.method == 'POST':
        form = SponsorProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('sponsor_front')
        else:
            messages.error(request, 'Error updating profile. Please check the form.')
    return redirect('sponsor_front')

@login_required
def participant_dashboard(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'PARTICIPANT':
        return redirect('index')
    from .models import Profile
    total_participants = Profile.objects.filter(role='PARTICIPANT').count()
    hackathon_data = {
        'national': {'title': 'National Level Hackathon', 'description': 'Participate in the nationwide competition with exciting prizes!'},
        'punjab': {'title': 'Punjab’s Hackathon', 'description': 'Showcase your talent at the state-level hackathon!'},
    }
    return render(request, 'participant_dashboard.html', {
        'total_participants': total_participants,
        'hackathon_data': hackathon_data,
        'role': 'PARTICIPANT'
    })
