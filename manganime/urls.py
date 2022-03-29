from django.urls import path
from manganime import views


urlpatterns = [
    path("", views.manganimes, name="manganimes"),
    path("<int:manganimeId>/", views.manganimeDetails, name="manganimeDetails"),
    path(
        "<int:manganimeId>/addBookmark",
        views.addBookmark,
        name="manganime-add-bookmark",
    ),  # post
    path(
        "<int:manganimeId>/deleteBookmark",
        views.deleteBookmark,
        name="manganime-delete-bookmark",
    ),  # post
    path(
        "<int:userId>/bookmark",
        views.getBookmark,
        name="manganime-get-bookmark",
    ), #get
]
