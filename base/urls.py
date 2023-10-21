from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static as stat



urlpatterns = [
    path('', views.endpoints),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('advocates/',views.AdvocateAPIView.as_view()),
    path('advocate-list/', views.advocates_list, name='advocate-list'),
    # path('advocates/<str:username>/', views.advocate_details),
    path('advocate-list/<str:username>/', views.AdvocateDetails.as_view()),

    path('companies/', views.companies_list, name='companies')
]

if settings.DEBUG:
    urlpatterns += stat(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)