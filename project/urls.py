"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from posts.views import post_list,post_detail,create_post,update_post,delete_post
from posts.views2 import Post_list,Post_detail,Create_post,Update_post,Delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('posts/',post_list),
    # path('create/',create_post),
    # path('details/<int:id>',post_detail),
    # path('update/<int:pk>',update_post),
    # path('delete/<int:id>',delete_post),
    path('posts/',Post_list.as_view()),
    path('create/',Create_post.as_view()),
    path('details/<int:pk>',Post_detail.as_view()),
    path('update/<int:pk>',Update_post.as_view()),
    path('delete/<int:pk>',Delete_post.as_view()),
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
