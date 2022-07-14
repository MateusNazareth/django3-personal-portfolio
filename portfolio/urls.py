from django.urls import path
from . import views

app_name = 'portfolio_app_name'

urlpatterns = [

    path('<int:proj_id>/', views.detail2, name="detail2"),
]
