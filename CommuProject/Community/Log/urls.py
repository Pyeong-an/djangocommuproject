from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main_page),#모든 로그 확인
    path('log/<int:lg>', views.log_detail),#서브로그확인
    path('confirm/<int:lg>', views.log_confirm),#수정
    path('modify/<int:lg>',views.log_modify),#수정
    path('delete/<int:lg>', views.log_delete)#삭제
]