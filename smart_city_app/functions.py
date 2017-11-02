from django.contrib.auth.models import Group, User
from smart_city_app.queries import *
# get the group_id of the user
def get_group_id(request, Group):
    if (request.user.is_authenticated()):
        groups = request.user.groups.all()
        if (len(groups) > 0):
            return Group.objects.raw(get_auth_group_id_by_name.format(groups[0]))[0].id

def get_user_by_id(user_id):
    return User.objects.raw(get_auth_user_by_id.format(user_id))

def get_group_id_by_name(group):
    return Group.objects.raw(get_auth_group_id_by_name.format(group))

