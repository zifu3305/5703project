from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from login import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


# router = DefaultRouter()
# router.register('login', views.LoginViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("login.urls")),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    # path("api/", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 获取Token的接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新Token有效期的接口
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证Token的有效性
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

