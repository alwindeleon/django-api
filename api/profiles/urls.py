from django.conf.urls import url, include

from .views import PersonalView
from .views import WorkView

app_name = "profiles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    url('pprofiles/', PersonalView.as_view()),
    url('wprofiles/', WorkView.as_view()),
]