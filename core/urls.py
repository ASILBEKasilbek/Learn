
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Login sahifasi
    path('logout/', views.user_logout, name='logout'),  # Logout yo‘li
    path('topic/<int:topic_id>/', views.question_detail, name='question_detail'),
    path('profile/', views.profile_edit, name='profile_edit'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)