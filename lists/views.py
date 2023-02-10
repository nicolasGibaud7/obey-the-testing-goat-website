from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, FormView

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List

# Create your views here.


class HomePageView(FormView):
    template_name = "home.html"
    form_class = ItemForm


class NewListView(CreateView, HomePageView):
    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)


class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = "list.html"
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)
