# forms/admin.py
from django.contrib import admin
from .models import WheelSpecification, WheelSpecificationFields

# Register main model
admin.site.register(WheelSpecification)

# Register nested fields model
admin.site.register(WheelSpecificationFields)

