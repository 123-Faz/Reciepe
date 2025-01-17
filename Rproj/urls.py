"""
URL configuration for Rproj project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Rapp.views import Reciepe1
from Rapp.views import deleterp
from Rapp.views import updaterp
from Rapp.views import login_page
from Rapp.views import register
from Rapp.views import logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Reciepe1/', Reciepe1,name='Reciepe1' ),
    path('deleterp/<int:id>/', deleterp, name='deleterp'),
    path('updaterp/<int:id>/', updaterp, name='updaterp'),
    path('login/', login_page,name='login_page' ),
    path('register/', register,name='register' ),
    path('logout/', logout_page, name='logout_page'),
    #path('', include('Rapp.urls')),
    
]

if settings.DEBUG:  # Now `settings` is properly defined
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)