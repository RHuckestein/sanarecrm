from django.urls import path
from refferal_accounts import views as refferal_accounts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tutorials_views.index, name='home'),
    path('', refferal_accounts_views.index.as_view(), name='home'),
    path('api/refferal_accounts/', refferal_accounts_views.tutorial_list),
    path('api/refferal_accounts/<int:pk>/', refferal_accounts_views.tutorial_detail),
    path('api/refferal_accounts/published/', refferal_accounts_views.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)