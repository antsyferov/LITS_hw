from django.conf.urls import url
from accounts.views import IndexView, UserListView, UserDetailView, UserAddView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^users/$', UserListView.as_view(), name='user_list'),
    url(r'^users/add/$', UserAddView.as_view(), name='user_add'),
    url(r'^users/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
]