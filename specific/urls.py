from specific.views import *
from django.urls import path

app_name='sad'
urlpatterns=[
    path('oneside/',oneside,name='oneside'),
    path('commited/',commited,name='commited'),
    path('breakup/',breakup,name='breakup'),
    path('singles/',singles,name='singles'),
]