from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('particles.json', TemplateView.as_view(template_name='particles.json', content_type='text/json'), name='particles_json'),
]