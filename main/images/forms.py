from django import forms

from images.models import ImageModel


class ImageForm(forms.ModelForm):
    image_file = forms.FileField()

    def save(self, commit=True):
        if self.files:
            self.instance.update_images_params()
        return super().save(commit=commit)

    class Meta:
        model = ImageModel
        fields = ["title", "description", "image_file"]
        widgets = {
            "image_file": forms.ClearableFileInput(),
        }
