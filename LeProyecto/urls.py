from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', include('MyApp.urls')),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('change-password/', auth_views.PasswordChangeView.as_view()),
  path('login/', auth_views.LoginView.as_view()),


]
