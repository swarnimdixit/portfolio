
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs', jobs.views.home, name='jobs/home.html'),
    path('blog', blog.views.blogpost, name='blog/home.html'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
