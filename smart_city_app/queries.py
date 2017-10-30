map_search = 'SELECT * FROM smart_city_app_map_item WHERE map_item_name LIKE \'%%{}%%\' AND map_item_address LIKE \'%%{}%%\';'
get_10_items = "SELECT * FROM smart_city_app_map_item WHERE map_item_type_id={} LIMIT 10;"
select_user = "SELECT * FROM auth_user WHERE id = {}"
