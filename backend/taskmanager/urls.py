from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),                  # Panel admin
    path('api/', include('tasks.urls')),              # Rutas de tareas

    # JWT endpoints (autenticación)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # login con username y password
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),     # renovar token
]
