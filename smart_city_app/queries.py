map_search = 'SELECT * FROM smart_city_app_map_item WHERE map_item_name LIKE \'%%{}%%\' AND map_item_address LIKE \'%%{}%%\';'
get_10_items = "SELECT * FROM smart_city_app_map_item WHERE map_item_type_id={} LIMIT 10;"
update_map_items = "UPDATE smart_city_app_map_item SET map_item_name='{}', map_item_address='{}', map_item_industry_type='{}', map_item_department='{}', map_item_email='{}', map_item_phone='{}', map_item_type_id={} WHERE map_item_id={};"
insert_map_item = "INSERT INTO smart_city_app_map_item (map_item_name, map_item_address, map_item_industry_type, map_item_department, map_item_email, map_item_type_id, map_item_phone) VALUES ('{}','{}','{}','{}','{}',{},'{}');"

get_map_item_by_id = "SELECT * FROM db.get_places WHERE map_item_id={}"
get_all_places = "SELECT * FROM db.get_places;"

select_user = "SELECT * FROM auth_user WHERE id = {}"
update_user = "UPDATE auth_user SET first_name='{}', last_name='{}', username='{}', email='{}' WHERE id={};"
insert_user = "INSERT INTO auth_user (username, password, first_name, last_name, email, is_superuser, is_staff, is_active, date_joined) VALUES ('{}','','{}','{}','{}', 0, 0, 1, '2017-11-01')"
get_auth_user_by_id = "SELECT * FROM auth_user WHERE id={};"
get_user_by_username = "SELECT * FROM auth_user WHERE username = '{}';"
get_all_auth_users = "SELECT * FROM auth_user;"

update_user_group_by_user_id = "UPDATE auth_user_groups SET group_id={} WHERE id={};"
get_group_id_by_user_id = "SELECT id FROM auth_user_groups WHERE user_id={}"
insert_into_auth_user_groups = "INSERT INTO auth_user_groups (group_id, user_id) VALUES ({},{});"

get_auth_group_by_name = "SELECT * FROM auth_group  WHERE name = '{}';"
get_auth_group_id_by_name = "SELECT id FROM auth_group  WHERE name = '{}';"
get_auth_groups = "SELECT * FROM auth_group"



