from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'theaters', views.TheaterViewSet)
router.register(r'productions', views.ProductionViewSet)
router.register(r'states', views.StateNameViewSet)

urlpatterns = [
    path('', views.index, name='theaters'),
    path('index', views.index, name='theaters'),
    path('productions/<int:tid>', views.productions, name='productions'),
    path('new_production', views.new_production, name='new_production'),
    path('search', views.search, name='search'),
    path('json', views.json, name='json'),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
]