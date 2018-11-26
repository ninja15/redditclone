from django.conf.urls import url
from . import views


app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'^user/(?P<ik>[0-9]+)', views.post_by, name='post_by'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
]