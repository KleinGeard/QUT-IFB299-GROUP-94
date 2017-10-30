# get the group_id of the user
def get_group_id(request, Group):
    if (request.user.is_authenticated()):
        groups = request.user.groups.all()
        if (len(groups) > 0):
            return Group.objects.raw("SELECT id FROM auth_group WHERE name='{}'".format(groups[0]))[0].id