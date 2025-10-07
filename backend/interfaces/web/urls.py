from django.urls import path
from .views import home_view, about_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('hakkimizda/', about_view, name='about'),
    path('iletisim/', contact_view, name='contact'),
]