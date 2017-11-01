map_search = 'SELECT * FROM smart_city_app_map_item WHERE map_item_name LIKE \'%%{}%%\' AND map_item_address LIKE \'%%{}%%\';'
get_10_items = "SELECT * FROM smart_city_app_map_item WHERE map_item_type_id={} LIMIT 10;"
select_user = "SELECT * FROM auth_user WHERE id = {}"
update_map_items = "UPDATE smart_city_app_map_item SET map_item_name='{}', map_item_address='{}', map_item_industry_type='{}', map_item_department='{}', map_item_email='{}', map_item_phone='{}', map_item_type_id={} WHERE map_item_id={};"
insert_map_item = "INSERT INTO smart_city_app_map_item (map_item_name, map_item_address, map_item_industry_type, map_item_department, map_item_email, map_item_type_id, map_item_phone) VALUES ('{}','{}','{}','{}','{}',{},'{}');"
update_user = "UPDATE auth_user SET first_name='{}', last_name='{}', username='{}', email='{}' WHERE id={};"
insert_user = "INSERT INTO auth_user (username, password, first_name, last_name, email, is_superuser, is_staff, is_active, date_joined) VALUES ('{}','{}','{}','{}','{}', 0, 0, 1, 0)"