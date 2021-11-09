from django.urls import path

from .views import UserListCreateView, UserAddAvatarView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_add_avatar')

]
