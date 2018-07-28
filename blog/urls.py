from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^page/(\d+)',views.page,name='page'),
    url(r'^editpage/(\d+)',views.edit_page,name='editpage'),
    url(r'^editaction/',views.edit_action,name='editaction')
]