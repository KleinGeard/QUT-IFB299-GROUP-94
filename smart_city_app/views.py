from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from smart_city_app.models import map_item
from smart_city_app.queries import map_search, get_10_items, update_map_items, insert_map_item, update_user, insert_user
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from smart_city_app.functions import get_group_id
from time import sleep

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

def profile_editor(request):
    page_title = 'Smart City - Profile Editor'

    u_id = request.GET.get('id') #from URL pattern

    username = ""
    first_name = ""
    last_name = ""
    email = ""
    account_type = ""
    password = ""

    u = 0
    count = 0

    if (u_id == None):
        u_id = 0

    group = ""
    groups = ""

    if (int(u_id) > 0):
        u = User.objects.raw("SELECT * FROM auth_user WHERE id={};".format(u_id))
        count = len(list(u))
        u = list(u)[0]
        user = User.objects.get(id = u_id)
        groups = user.groups.all()
        if (len(list(groups))):
            group = groups[0].name
        else:
            group = "No group"

    if (request.method == "POST"):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        group = request.POST.get('account_type')
        password = request.POST.get('password')
        #update database
        if (group != None):
            auth_group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(group))
            if (len(list(auth_group_id))):
                auth_group_id = list(auth_group_id)[0].id
                with connection.cursor() as cursor:
                    cursor.execute(update_user.format(first_name, last_name, username, email, u_id))
                    if (group.lower() == "administration" or group.lower() == "students" or group.lower() == "businessmen" or group.lower() == "tourists"):
                        if (len(list(groups))):
                            cursor.execute("SELECT id FROM auth_user_groups WHERE user_id={}".format(u_id))
                            user_group_id = cursor.fetchall()[0]
                            cursor.execute("UPDATE auth_user_groups SET group_id={} WHERE id={};".format(auth_group_id, int(user_group_id[0])))
                            print("updated")
                        else:
                            cursor.execute(insert_user.format(username, password, first_name, last_name, email))
                            sleep(2.0)
                            relevant_user = User.objects.raw("SELECT * FROM auth_user WHERE username = '{}';".format(username))
                            sleep(0.5)
                            relevant_group_table = Group.objects.raw("SELECT * FROM auth_group  WHERE name = '{}';".format(group))
                            sleep(0.5)
                            cursor.execute("INSERT INTO auth_user_groups (group_id, user_id) VALUES ({},{});".format(list(relevant_group_table)[0].id, list(relevant_user)[0].id))
                            print("inserted")

        return HttpResponseRedirect("/administration")

    group_id = get_group_id(request, Group)

    if (group_id == 1):
        return render(request, "smart_city_app/profile_editor.html",
        {
            "page_title": page_title,
            "group_id": group_id,
            "u": u,
            "user_group": group,
        })
    else:
        return render(request, "smart_city_app/oops.html",{})

def editor(request):
    page_title = 'Smart City - Editor'
    group_id = 0
    place_id = request.GET.get('id')

    name = ""
    addr = ""
    ind = ""
    depart = ""
    email = ""
    phone = ""
    group = "" 

    place = 0
    count = 0

    if (place_id == None):
        place_id = 0

    if (int(place_id) > 0):
        place = map_item.objects.raw("SELECT * FROM db.get_places WHERE map_item_id={};".format(place_id))
        count = len(list(place))
        place = list(place)[0]

    if (request.method == "POST"):
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        ind = request.POST.get('ind')
        depart = request.POST.get('depart')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        group = request.POST.get('group')  

        if (int(place_id) > 0):
            auth_group_id = 0
            if (group != None):
                auth_group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(group))
                auth_group_id = list(auth_group_id)[0].id
            with connection.cursor() as cursor:
                cursor.execute(update_map_items.format(name, addr, ind, depart, email, phone, int(auth_group_id), int(place_id)))
            return HttpResponseRedirect("/places")
        else:
            auth_group_id = 0
            if (group != None):
                auth_group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(group))
                auth_group_id = list(auth_group_id)[0].id
            with connection.cursor() as cursor:
                cursor.execute(insert_map_item.format(name, addr, ind, depart, email, int(auth_group_id), phone))
            return HttpResponseRedirect("/places")

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

    results = map_item.objects.raw("SELECT * FROM db.get_places;") # selecting from a view, joining map_items and auth_group
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

def administration(request):
    page_title = 'Smart City - administration'

    results = User.objects.raw("SELECT * FROM auth_user;")

    group_id = get_group_id(request, Group)
    if (group_id == 1):
        return render(request, "smart_city_app/administration.html",
        {
            # Pass variables into template
            "page_title": page_title,
            "group_id": group_id,
            "results": results,
        })
    else:
        return render(request, "smart_city_app/oops.html",{})

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

def profile(request):
    page_title = "Smart City - Your Profile"

    group = ""
    groups = request.user.groups.all()
    if (len(list(groups))):
        group = groups[0].name
    else:
        group = "No group"

    if (request.user.is_authenticated()):
        return render(request, "smart_city_app/profile.html",
        {
            # Pass variables into template
            "page_title": page_title,
            "group_id": get_group_id(request, Group),
            "user_group": group
        })
    else:
        return render(request, "smart_city_app/oops.html",{})

def edit_profile(request):
    page_title = 'Smart City - Edit Profile Info'
    group_id = 0
    place_id = request.GET.get('id')
    group = "" 

    place = 0
    count = 0

    if (place_id == None):
        place_id = 0

    if (int(place_id) > 0):
        place = map_item.objects.raw("SELECT * FROM db.get_places WHERE map_item_id={}".format(place_id))
        count = len(list(place))
        place = list(place)[0]

    user_group = ""
    groups = request.user.groups.all()
    if (len(list(groups))):
        user_group = groups[0].name
    else:
        user_group = "No group"

    if (request.method == "POST"):
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        group = request.POST.get('group')  

        auth_group_id = 0
        if (group != None):
            auth_group_id = Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(group))

            if (len(list(auth_group_id))):
                auth_group_id = list(auth_group_id)[0].id
                with connection.cursor() as cursor:
                    cursor.execute(update_user.format(first_name, last_name, username, email, int(request.user.id)))
                    if (group.lower() == "students" or group.lower() == "businessmen" or group.lower() == "tourists"):
                        if (len(list(groups))):
                            cursor.execute("SELECT id FROM auth_user_groups WHERE user_id={}".format(request.user.id))
                            user_group_id = cursor.fetchall()[0]
                            cursor.execute("UPDATE auth_user_groups SET group_id={} WHERE id={};".format(auth_group_id, int(user_group_id[0])))
                            print("updated")
                        else:
                            cursor.execute("INSERT INTO auth_user_groups (group_id, user_id) VALUES ({},{});".format(auth_group_id, request.user.id))
                            print("inserted")

        return HttpResponseRedirect("/profile")

    group_id = get_group_id(request, Group)

    with connection.cursor() as cursor:
        group_list = cursor.execute("SELECT * FROM auth_group")

    user_group = ""
    groups = request.user.groups.all()
    if (len(list(groups))):
        user_group = groups[0].name
    else:
        user_group = "No group"

    if (request.user.is_authenticated()):
        return render(request, "smart_city_app/edit-profile.html",
        {
            # Pass variables into template
            "page_title": page_title,
            "user_group": user_group,
            "group_id": get_group_id(request, Group),
            "group_list": group_list
        })
    else:
        return render(request, "smart_city_app/oops.html",{})