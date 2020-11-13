"""medik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet
from bot.views import Chat, IllnessClassifier, SymptomsList
from diets.views import DietView

router = DefaultRouter()

router.register('news', ArticleViewSet, 'news')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/chat/', Chat.as_view()),
    path('api/illness/', IllnessClassifier.as_view()),
    path('api/diets/', DietView.as_view()),
    path('api/symptoms/', SymptomsList.as_view())
]
