from django.urls import path
from . import views

app_name = 'accounts'

# URLConf
urlpatterns = [
  path('', views.index, name="accounts")
]