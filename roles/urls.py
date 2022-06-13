from django.urls import path

from roles.views import RoleListView, RoleDetailView, RoleCreateView, RoleEditView

app_name = 'roles'

urlpatterns = [
    path('list/', RoleListView.as_view(), name='list'),
    path('details/<int:pk>/', RoleDetailView.as_view(), name='details'),
    path('create/', RoleCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', RoleEditView.as_view(), name='edit')
]
