from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main_page),
    path('log/<int:lg>', views.log_detail)
]