from django.contrib import admin
from . models import *

admin.site.register(user_details)
admin.site.register(owner_details)
admin.site.register(place)
admin.site.register(building_details)
admin.site.register(booking)
admin.site.register(payment)
admin.site.register(review_rating)
