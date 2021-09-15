from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get_popular_survey/', views.get_popular_survey, name="get_popular_survey"),
    path('get_all_surveys/', views.get_all_surveys, name="get_all_surveys"),
    path('submit_survey/', views.submit_survey, name="submit_survey"),
    path('<str:partial_view>/', views.index, name="index/partial_view"),
    path('<str:partial_view>/<int:pk>', views.index, name="index/partial_view/id"),
]
