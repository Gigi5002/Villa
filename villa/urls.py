from django.urls import path
from .views import index_view, VillaListView, villa_detail_view, villa_update_view, villa_delete_view

urlpatterns = [
    path('', index_view, name='index'),  # Главная страница как корневой URL
    path('index/', index_view, name='index_alt'),  # Альтернативный URL для главной
    path('villa_list/', VillaListView.as_view(), name='villa_list'),
    path('villa_detail/<int:pk>/', villa_detail_view, name='villa_detail'),
    path('villa_update/<int:pk>/', villa_update_view, name='villa_update'),
    path('villa_delete/<int:pk>/', villa_delete_view, name='villa_delete'),
]
