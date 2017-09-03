from django.shortcuts import render
from django.http import HttpResponse

# Welcome/home page view
def index(request):
    page_title = 'Smart City - Welcome Page'
    
    location = request.GET.get('city') # Stored as a url parameter so users can bookmark the url with a specific city
    q = request.POST.get('query') # Retrieve map search query from text field

    # Only update the session variable if it's not empty
    if (q != None and q != ''):
        request.session['query'] = q

    # If none of the valid cities, set to Australia
    if (location != 'Brisbane' and location != 'Sydney' and location != 'Perth' and location != 'Hobart'):
        location = 'Australia' # I know it's not a city btw

    # TODO: get results from database and compare with query, then construct list
    results = {'Queensland University of Technology','University of Queensland', 'Test location', 'A museum somewhere', 'Cinema'}

    # Construct the markup based on the template, and variables
    return render(request, "smart_city_app/index.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "location": location,
        "query": request.session['query'],
        "results": results,
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
