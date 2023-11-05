from django.urls import path
from . import views

urlpatterns = [
    # path('', views.gallery, name='gallery'),
    path('', views.HandbagListView.as_view(), name='gallery'),
    # path('photo/<str:pk>', views.viewPhoto, name='photo'),
    path('photo/<str:pk>', views.HandbagDetailView.as_view(), name='photo'),
    # path('add/', views.addPhoto, name='add'),
    path('add/', views.HandbagCreate.as_view(), name='add'),
]
