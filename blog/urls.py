from django.urls import path
from . import views

urlpatterns = [
    # ❌ 잘못된 코드: path(' <int:pk>/', ... ) 또는 path('<int:pk> /', ...) 같은 공백이 있는지 확인
    # ✅ 올바른 코드: 꺾쇠 앞뒤로 공백이 없어야 합니다.
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]