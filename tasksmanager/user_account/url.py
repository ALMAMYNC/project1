from django.contrib import admin
from django.urls import path, include
from user_account.views import signin, signup, signout, tasks


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tasks, name='tasks'),
    path("login/", signin, name='signin'),
    path("register/", signup, name='signup'),
    path("logout/", signout, name='signout'),
]
