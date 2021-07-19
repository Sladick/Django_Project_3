from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('news.urls')),
    path('captcha/', include('captcha.urls')),
    path('testapp/', include('testapp.urls')),
    path('weather/', include('weather.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
