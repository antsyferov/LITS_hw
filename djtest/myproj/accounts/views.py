from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from accounts.models import FakeUser
from accounts.forms import FuserForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['my_var'] = 'my var'
        context['fakes'] = FakeUser.objects.all()
        return context

class UserListView(ListView):
    template_name = 'user_list.html'
    model = FakeUser


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = FakeUser

class UserAddView(TemplateView):
    template_name = 'user_add.html'

    def get(self, request):
        user_form = FuserForm()
        return self.render_to_response(context={'form': user_form})

    def post(self, request):
        user_form = FuserForm(data=request.POST)
        if user_form.is_valid():
            FakeUser.objects.create(name=user_form.cleaned_data['name'])
            return HttpResponseRedirect('/')
        return self.render_to_response(context={'form': user_form})


