from django.urls import path

from profile import views

urlpatterns = [
    path("", views.homeUsers, name="view-profile"),  # page de profile : profile/
    path("edit/", views.edit, name="view-edit"),  # get post
    path("admin/", views.admin, name="view-admin"),  # get
    # path('admin/<int:profil_id>', views.adminDetail), #get et post
    path("admin/<int:profil_id>/edit", views.adminEdit),  # get et post
    path(
        "admin/<int:profil_id>/remove", views.adminRemove, name="delete-admin"
    ),  # post
]
