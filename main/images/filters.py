import django_filters as df

from images.models import ImageModel


class ImagesFilter(df.FilterSet):
    image_height__gt = df.NumberFilter(field_name='image_height', lookup_expr='gt', label="height >")
    image_height__lt = df.NumberFilter(field_name='image_height', lookup_expr='lt', label="height <")

    image_width__gt = df.NumberFilter(field_name='image_width', lookup_expr='gt', label="width >")
    image_width__lt = df.NumberFilter(field_name='image_width', lookup_expr='lt', label="width <")

    title = df.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ImageModel
        fields = ['title']