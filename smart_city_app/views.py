from django.shortcuts import render
from django.http import HttpResponse
from smart_city_app.models import map_item
from smart_city_app.queries import map_search

# Welcome/home page view
def index(request):
    page_title = 'Smart City - Welcome Page'

    # initialize set of results
    results = []
    # if no search has occurred (this is the purpose of -1), don't display any text, if 0, 
    # display "No results found", else it'll display "Results for..."
    result_count = -1

    location = request.GET.get('city') # Stored as a url parameter so users can bookmark the url with a specific city
    q = request.POST.get('query') # Retrieve map search query from text field

    # Construct the map file name
    map_image = ''
    if (location != None):
        map_image = location.lower() + '-map.PNG'

    # Only update the session variable if it's not empty
    if (q != None and q != ''):
        request.session['query'] = q
        
        results = map_item.objects.raw(map_search.format(q))
        result_count = len(list(results))
    
    # If none of the valid cities, set to Australia
    if (location != 'Brisbane' and location != 'Sydney' and location != 'Perth' and location != 'Hobart'):
        location = 'Australia' # I know it's not a city btw

    # TODO: get results from database and compare with query, then construct list
    
    # Construct the markup based on the template, and variables
    return render(request, "smart_city_app/index.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "location": location,
        "map": map_image,
        "query": request.session['query'],
        "results": results,
        "len":result_count,
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
