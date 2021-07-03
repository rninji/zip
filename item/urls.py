from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeitem, name="homeitem"),
    path('new/', views.newitem, name="newitem"),
    path('detail/<int:index>', views.detailitem, name="detailitem"),
    path('edit/<int:index>', views.edititem, name="edititem"),
    path('detail/<int:pk>/delete', views.deleteitem, name="deleteitem"),
    path('detail/<int:index>/comment/<int:comment_pk>/delete/',
         views.delete_comment, name="delete_comment"),
    # path('like/<int:item_id>',views.like_item,name="like_item"),
]
