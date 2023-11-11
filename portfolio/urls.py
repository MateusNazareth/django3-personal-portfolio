from django.urls import path
from . import views

app_name = 'portfolio_app_name'

urlpatterns = [

    path('<int:proj_id>/', views.detail2, name='detail2'),

]

    # path('projeto1', views.projeto1, name='projeto1'),
    # path('projeto2', views.projeto2, name='projeto2'),
    # path('projeto3', views.projeto3, name='projeto3'),
    # path('projeto4', views.projeto4, name='projeto4'),
