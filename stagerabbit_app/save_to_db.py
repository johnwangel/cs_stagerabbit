import sys, os, django

from django.conf import settings
settings.configure(DEBUG=True)

sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()

from stagerabbit_app.models import MyModel