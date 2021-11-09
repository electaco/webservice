from django.urls import path

from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('get/<int:id>', views.get_markers, name='get_markers'),
    path('<int:id>/download', views.download_markers, name='download_markers'),
    path('<int:id>', views.marker, name='info_markers'),
    path('', views.index, name='index'),
    path('upload/', views.submit_markers, name='submit_markers'),
]