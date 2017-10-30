from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from smart_city_app.models import map_item
from smart_city_app.queries import map_search
from smart_city_app.queries import get_10_items
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from smart_city_app.functions import get_group_id

# Welcome/home page view
def index(request):
    
    # u = User.objects.get(username='dev') 
    # u.set_password('dev') # getting around the password requirements
    # u.save()

    page_title = 'Smart City - Welcome Page'
    group_id = 0
    top_ten = {}
    results = []
    # if no search has occurred (this is the purpose of -1), don't display any text, if 0, 
    # display "No results found", else it'll display "Results for..."
    result_count = -1

    location = request.GET.get('city') # Stored as a url parameter so users can bookmark the url with a specific city
    q = request.POST.get('query') # Retrieve map search query from text field
    
    if (request.user.is_authenticated()):
        groups = request.user.groups.all()
        if (len(groups) > 0):
            group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}';".format(groups[0].name))[0].id
            top_ten = map_item.objects.raw(get_10_items.format(group_id))

    if (q):
        request.session['query'] = q
        results = map_item.objects.raw(map_search.format(q,location))
        result_count = len(list(results))
    
    if (location != 'Brisbane' and location != 'Sydney' and location != 'Perth' and location != 'Hobart'):
        location = 'Australia'

    top_ten_len = len(list(top_ten))

    latitude = request.POST.get('lat')
    longitude = request.POST.get('long')

    request_type = ""
    if request.method == 'POST':
        if request.POST.get("search"):
            request_type = "search"
        elif request.POST.get("directions"):
            request_type = "directions"

    # Construct the markup based on the template, and variables
    return render(request, "smart_city_app/index.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "location": location,
        "results": results,
        "len":result_count,
        "top_ten":top_ten,
        "top_ten_len":top_ten_len,
        "group_id":group_id,
		"query":q,
        "latitude":latitude,
        "longitude":longitude,
        "request_type":request_type,
    })

def editor(request):
    page_title = 'Smart City - Editor'
    group_id = 0
    place_id = request.GET.get('id')

    place = 0
    count = 0

    if (place_id == None):
        place_id = 0

    if (int(place_id) > 0):
        place = map_item.objects.raw("SELECT * FROM smart_city_app_map_item WHERE map_item_id={}".format(place_id))
        count = len(list(place))
        place = list(place)[0]

    group_id = get_group_id(request, Group)

    if (group_id == 1):
        return render(request, "smart_city_app/editor.html",
        {
            # Pass variables into template
            "page_title": page_title,
            "place": place,
            "place_id": int(place_id), # For some reason it's not always an integer, so this solves that!
            "count": count,
            "group_id": group_id,
        })
    else:
        return render(request, "smart_city_app/oops.html",{})

def places(request):
    page_title = 'Smart City - Places'

    results = map_item.objects.raw("SELECT * FROM db.get_places;")
    count = len(list(results))

    group_id = get_group_id(request, Group)

    if (group_id == 1):
        return render(request, "smart_city_app/places.html",
        {
            # Pass variables into template
            "page_title": page_title,
            "group_id": group_id,
            "results": results,
            "count": count
        })
    else:
        return render(request, "smart_city_app/oops.html",{})

def about(request):
    page_title = 'Smart City - about'
    group_id = get_group_id(request, Group)

    return render(request, "smart_city_app/about.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "group_id": group_id,
    })

def contact(request):
    page_title = 'Smart City - contact'
    group_id = get_group_id(request, Group)

    return render(request, "smart_city_app/contact.html",
    {
        # Pass variables into template
        "page_title": page_title,
        "group_id": group_id,
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
