from django.contrib import admin
from finder.models import *
from company.models import *
from offers.models import *

admin.site.register(Finder)
admin.site.register(Company)
admin.site.register(Offer)
admin.site.register(Category)
admin.site.register(Feedback)

# Register your models here.
