from django.urls import path
from . import views

urlpatterns = [
    path('', views.HandbagListView.as_view(), name='gallery'),
    path('photo/<str:pk>', views.HandbagDetailView.as_view(), name='photo'),
    path('add/', views.HandbagCreate.as_view(), name='add'),
    path('photo/<str:pk>/delete', views.HandbagDeleteView.as_view(), name='delete_handbag'),
    path('photo/<str:pk>/update', views.HandbagUpdateView.as_view(), name='update_handbag'),
]
