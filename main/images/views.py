from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from images.filters import ImagesFilter
from images.forms import ImageForm
from images.models import ImageModel


class ListImages(LoginRequiredMixin, FilterView):
    template_name = "list.html"
    paginate_by = settings.PAGINATE_BY
    queryset = ImageModel.objects.all()
    filterset_class = ImagesFilter


class CreateImage(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    model = ImageModel
    form_class = ImageForm
    success_url = reverse_lazy("images:list_images")


class UpdateImage(LoginRequiredMixin, UpdateView):
    template_name = "update.html"
    model = ImageModel
    form_class = ImageForm
    success_url = reverse_lazy("images:list_images")


class DeleteImage(LoginRequiredMixin, DeleteView):
    template_name = "delete.html"
    model = ImageModel
    success_url = reverse_lazy("images:list_images")
