from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from users.views import createGroup, home, delete, add, leave, post, timeline, deletePosts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('createGroup', createGroup, name='createGroup'),
    path('delete', delete, name='delete'),
    path('add', add, name='add'),
    path('leave', leave, name='leave'),
    path('post', post, name='post'),
    path('home', home, name='home'),
    path('timeline', timeline, name='timeline'),
    path('deletePosts', deletePosts, name='deletePosts'),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
