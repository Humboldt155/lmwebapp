from django.conf.urls import url
from complements.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]