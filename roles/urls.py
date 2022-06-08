from django.urls import path

from roles.views import RoleListView, RoleDetailView

app_name = 'roles'

urlpatterns = [
    path('list/', RoleListView.as_view(), name='RoleList'),
    path('details/<int:pk>/', RoleDetailView.as_view(), name='RoleDetails')
]
