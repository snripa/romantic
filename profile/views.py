# coding: utf-8
# author: dlyapun

# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from materials.models import Material
from power_comments.models import PowerComment
from profile.forms import UserCreateForm, UserLoginForm, CustomUserForm
from profile.models import CustomUser


class ProfileListView(ListView):
    model = CustomUser
    context_object_name = 'users'


class ProfileDetailView(DetailView):
    model = CustomUser

    context_object_name = 'profile'


class RegisterFormView(FormView):
    form_class = UserCreateForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/registration_complete/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration_form.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        last_user = CustomUser.objects.last()
        # Выполняем аутентификацию пользователя.
        last_user.user.is_active = False
        last_user.user.save()

        # login(self.request, self.user)

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


    # def get_form_kwargs(self):
    #     kwargs = super(RegisterFormView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs


    # def get_form(self, form_class):
    #     return form_class(**self.get_form_kwargs())


    # def get(self, request, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect("/blog/")
    #     else:
    #         return self.render_to_response(self.get_context_data(), **kwargs)


class LoginFormView(FormView):
    form_class = UserLoginForm
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"
    # В случае успеха перенаправим на главную.
    success_url = "/blog/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


    # def get_form(self, form_class):
    #     return form_class(**self.get_form_kwargs())
 

    # def get(self, request, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect("/blog/")
    #     else:
    #         return self.render_to_response(self.get_context_data(), **kwargs)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/blog/")


def government(request):
    users = CustomUser.objects.filter(goverment=True)
    data = {'users': users}
    return render_to_response('profile/government.html',
                              data,
                              context_instance=RequestContext(request))


@login_required
def profile_edit(request):
    profile = CustomUser.objects.get(user=request.user)

    template = 'profile_edit.html'

    if request.POST:    # If the form has been submitted...
        form = CustomUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():     # All validation rules pass
            form.save()
            url = u'/profile/%s' % profile.id
            return redirect(url)
        else:
            return render_to_response(template, {
                                      'form': form,
                                      'profile': profile},
                                      context_instance=RequestContext(request))
    else:
        form = CustomUserForm(
            instance=profile,
            initial={
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'email': profile.user.email,
            })
    return render_to_response(template, {
                              'form': form,
                              'profile': profile},
                              context_instance=RequestContext(request))


def profile(request, profile_id):
    profile2 = CustomUser.objects.get(id=profile_id)
    comments = PowerComment.objects.filter(owner=profile2).order_by('-date_creation')[:10]
    materials = Material.objects.filter(owner=profile2).exclude(state=2) 

    material_enable = Material.objects.filter(owner=profile2, state=1)
    material_disable = Material.objects.filter(owner=profile2, state=0)

    articles_disable = _get_articles(material_disable)
    articles_enable = _get_articles(material_enable)

    reports_disable = _get_reports(material_disable)
    reports_enable = _get_reports(material_enable)
    
    data = {'profile2': profile2, 'comments': comments,
            'articles_disable': articles_disable, 'articles_enable': articles_enable,
            'reports_disable': reports_disable, "reports_enable": reports_enable,}
    return render_to_response('profile.html',
                              data,
                              context_instance=RequestContext(request))


def _get_articles(materials):    
    articles = []

    for material in materials:
        if material.rank == 1 or material.rank == 3 or material.rank == 4:
            articles.append(material)
        else:
            pass    

    return articles


def _get_reports(materials):    
    reports = []

    for material in materials:
        if material.rank == 0 or material.rank == 2:
            reports.append(material)
        else:
            pass    

    return reports
