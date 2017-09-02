from django.shortcuts import render
from django.http import HttpResponse

# Welcome/home page view
def index(request):
    page_title = 'Smart City - Welcome Page'
    
    # Get the selected location
    location = request.GET.get('city')

    # If none of the valid cities, set to Australia
    if (location != 'Brisbane' and location != 'Sydney' and location != 'Perth' and location != 'Hobart'):
        location = 'Australia'

    return render(request, "smart_city_app/index.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "location": location
    })

def about(request):
    page_title = 'Smart City - about'

    return render(request, "smart_city_app/about.html",
    {
        # Pass variables into template
        "page_title": page_title
        
    })

def contact(request):
    page_title = 'Smart City - contact'

    return render(request, "smart_city_app/contact.html",
    {
        # Pass variables into template
        "page_title": page_title
        
    })
    
def login(request):
    page_title = 'Smart City - Login'

    return render(request, "smart_city_app/login.html",
    {
        # Pass variables into template
        "page_title": page_title
        
    })

def register(request):
    page_title = 'Smart City - Registration'

    return render(request, "smart_city_app/register.html",
    {
        # Pass variables into template
        "page_title": page_title
        
    })
