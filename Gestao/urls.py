from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('add-category', views.admin_add_category_view(), name="add-category"),
    path('view-category-', views.admin_view_category_view(), name="view-category"),
    path('category-view', views.admin_category_view, name="add-category"),
    path('delete-category', views.delete_category_view(), name="delete-category"),
    path('add-imposto', views.admin_category_view(),name='add-imposto'),
    path('view-imposto', views.admin_imposto_view(),name='view-imposto'),
]