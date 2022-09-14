from django.conf.urls.static import static
from django.urls import path, re_path

from coolsite import settings
from .views import *

urlpatterns = [
    path('', XboxHome.as_view(), name='home'),
    path('news/', XboxNews.as_view(), name='news'),
    path('sales/', XboxSales.as_view(), name='sales'),
    path('about_us/', XboxAboutUs.as_view(), name='about_us'),
    path('contacts/', XboxContacts.as_view(), name='contacts')]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)