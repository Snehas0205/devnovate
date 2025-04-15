from django.contrib import admin
from django.urls import path, include

# Customize admin site appearance
admin.site.site_header = 'Devnovate Administration'  # Header displayed on the admin page
admin.site.site_title = 'Devnovate Admin'  # Title for the browser tab
admin.site.index_title = 'Devnovate Admin Portal'  # Title displayed on the admin index page

urlpatterns = [
    path('admin/', admin.site.urls),  # Changed back to the default 'admin/' URL
    path('', include('core.urls')),  # Include the core app's URLs
]
