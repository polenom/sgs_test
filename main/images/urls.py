from django.urls import path

from images.views import CreateImage, UpdateImage, ListImages, DeleteImage

app_name = "images"
urlpatterns = [
    path("", ListImages.as_view(), name="list_images"),
    path("create/", CreateImage.as_view(), name="create_image"),
    path("<int:pk>/update/", UpdateImage.as_view(), name="update_image"),
    path("<int:pk>/delete/", DeleteImage.as_view(), name="delete_image"),
]
