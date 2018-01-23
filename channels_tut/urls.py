from django.conf.urls import url
from channels_tut.views import user_list, log_in, log_out, sign_up

app_name = 'channels_tut'
urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^login/$', log_in, name='log_in'),
    url(r'^signup/$', sign_up, name='sign_up'),
    url(r'^logout/$', log_out, name='log_out'),
]