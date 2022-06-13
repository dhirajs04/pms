from django.urls import path

from roles.role_permissions.views import RolePermissionsListView, RolePermissionDetailView

app_name = 'role_permissions'

urlpatterns = [
    path('list/', RolePermissionsListView.as_view(), name='list'),
    path('details/<int:pk>/', RolePermissionDetailView.as_view(), name='details')
]
