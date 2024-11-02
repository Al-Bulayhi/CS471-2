"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import apps.bookmodule.views
import apps.usermodule.views

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    #path('users/', include("apps.usermodule.urls"))
    path('', apps.bookmodule.views.index, name= "books.index"),
    path('list_books/', apps.bookmodule.views.list_books, name= "books.list_books"),
    path('<int:bookId>/', apps.bookmodule.views.viewbook, name="books.view_one_book"),
    path('aboutus/', apps.bookmodule.views.aboutus, name="books.aboutus"),
    
]
