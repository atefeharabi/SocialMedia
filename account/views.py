from django.shortcuts import render
from django.views import View
from .forms import RegisterForm


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})