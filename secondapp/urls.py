from django.urls import path

from secondapp.views import introduce

app_name = 'secondapp'

urlpatterns = [
    path('introduce/', introduce, name='introduce')
]
