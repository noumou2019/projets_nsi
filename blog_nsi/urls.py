from . import views 
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    
    path('', views.post),
    url(r'^post/(?P<id>[0-9]+)$',views.show_post),


    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 
