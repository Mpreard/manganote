from django.urls import path
from friendship import views


urlpatterns = [
    path('', views.friendsList, name="friends"),
    path('invites', views.invitesList, name="invites"),
    path('invites/<int:id_invitation>/delete', views.delete, name="delete"),
    path('invites/<int:id_invitation>/accept', views.accept, name="accept"),
    path('invites/invite', views.inviteFriend, name="invite"),
    path('watch/<int:id_user>', views.friendview, name="watch")
]