import json

from django.contrib.auth import get_user_model
from django.db import models

from images.services import get_average_color, get_palette_color, get_predominant_color

user_model = get_user_model()


def save_path_image(instance, filename):
    return f"images/{filename}"


def save_path_palette_color(instance, filename):
    return f"palette/{filename}"


class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image_file = models.ImageField(height_field="image_height", width_field="image_width", upload_to=save_path_image)
    image_height = models.PositiveIntegerField()
    image_width = models.PositiveIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    predominant_color = models.CharField(max_length=7)
    average_color = models.CharField(max_length=7)
    palette_color = models.JSONField()

    def update_images_params(self):
        self.palette_color = get_palette_color(self.image_file)
        self.average_color = get_average_color(self.image_file)
        self.predominant_color = get_predominant_color(self.image_file)
