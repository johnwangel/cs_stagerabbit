from django.contrib import admin

from .models import Theater
from .models import Production
from .models import State

admin.site.register(Theater)
admin.site.register(Production)
admin.site.register(State)