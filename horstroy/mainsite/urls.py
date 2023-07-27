from django.urls import path, include

from .views import index, services, technologies, materials, portfolio, designs

urlpatterns = [
    path('services/', services, name='services'),
    path('technologies/', technologies, name='technologies'),
    path('materials/', materials, name='materials'),
    path('portfolio/', portfolio, name='portfolio'),
    path('designs/', designs, name='designs'),
    path('', index, name='index'),
]
