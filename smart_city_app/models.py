from django.db import models

# Using the same model for all of the item types
class map_item(models.Model):
    map_item_id = models.AutoField(primary_key=True)
    map_item_name = models.CharField(max_length=50)
    map_item_address = models.CharField(max_length=256)
    map_item_phone = models.CharField(max_length=50)
    map_item_industry_type = models.CharField(max_length=256)
    map_item_department = models.CharField(max_length=256)
    map_item_email = models.CharField(max_length=256)

    def __unicode__(self):
        return self.map_item_name