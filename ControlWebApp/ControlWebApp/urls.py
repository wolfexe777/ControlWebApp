from django.contrib import admin
from django.urls import path
from ControlApp.views import post_list, post_detail,  post_new, post_edit, post_delete, comment_edit, comment_delete,comment_new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/new/', post_new, name='post_new'),
    path('posts/<int:id>/edit/', post_edit, name='post_edit'),
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),
    path('comments/<int:id>/delete/', comment_delete, name='comment_delete'),
    path('comments/<int:id>/edit/', comment_edit, name='comment_edit'),
    path('posts/<int:id>/comment/', comment_new, name='comment_new'),
]
