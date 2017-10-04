from django.shortcuts import render, redirect
from django.http import HttpResponse
from smart_city_app.models import map_item
from smart_city_app.queries import map_search
from smart_city_app.queries import get_10_items
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

# Welcome/home page view
def index(request):
    page_title = 'Smart City - Welcome Page'
    group_id = 0
    top_ten = {}

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
    
    if (request.user.is_authenticated()):
        groups = request.user.groups.all()
        if (len(groups) > 0):
            group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(groups[0]))[0].id
            top_ten = map_item.objects.raw(get_10_items.format(group_id))

    # Only update the session variable if it's not empty
    if (q):
        request.session['query'] = q
        
        results = map_item.objects.raw(map_search.format(q,location))
        result_count = len(list(results))
    
    # If none of the valid cities, set to Australia
    if (location != 'Brisbane' and location != 'Sydney' and location != 'Perth' and location != 'Hobart'):
        location = 'Australia' # I know it's not a city btw

    top_ten_len = len(list(top_ten))

    # Construct the markup based on the template, and variables
    return render(request, "smart_city_app/index.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "location": location,
        "map": map_image,
        "results": results,
        "len":result_count,
        "top_ten":top_ten,
        "top_ten_len":top_ten_len,
        "group_id":group_id,
		"query":q,
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

def register(request):
    page_title = 'Smart City - Registration'

    # https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, "smart_city_app/register.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "form": form,
    })
