from django.urls.base import reverse
from .models import Farmers
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    model = Farmers
    template_name = 'farmers/index.html'
    context_object_name = 'uploads'


class SingleView(DetailView):
    model = Farmers
    template_name = 'farmers/single.html'
    context_object_name = 'upload'


class PostsView(ListView):
    model = Farmers
    template_name = 'farmers/posts.html'
    context_object_name = 'post_list'


class AddView(LoginRequiredMixin, CreateView):
    model = Farmers
    template_name = 'farmers/add.html'
    fields = ['produce', 'Price_per_kilo', 'Location', 'Contacts', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Farmers
    template_name = 'farmers/edit.html'
    fields = ['produce', 'Price_per_kilo', 'Location', 'Contacts', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Farmers
    template_name = 'farmers/confirm-delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    # take user to post after submission
    success_url = reverse_lazy('farmers:posts')
