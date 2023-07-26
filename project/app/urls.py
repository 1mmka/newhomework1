from django.urls import path
from app.views import login,registration

urlpatterns = [
    path('',login,name='login'),
    path('registration',registration,name='registration')
]
