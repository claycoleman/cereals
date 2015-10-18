from django.shortcuts import render, render_to_response, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import RequestContext
from mmain.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mmain.forms import UserSignUp, UserLogin, Search, CreateCerealForm, UpdateCerealForm, CreateManufacturerForm
from django import forms
from django.core.mail import send_mail


def cereal_list(request):
    context = {}
    context['request'] = request

    request.META['HTTP_REFERER'] = '{% url "cereal_list" %}'
    context['cereals'] = Cereal.objects.all().order_by('name')
    print request.user
    form = Search(request.GET)
    if form.is_valid():
        print form.cleaned_data
        search = form.cleaned_data['search']
        context['cereals'] = Cereal.objects.filter(name__icontains=search).order_by('name')
        if search is None:
            context['cereals'] = Cereal.objects.all().order_by('name')
    context['length'] = len(context['cereals'])
    context['form'] = form

    return render_to_response('cereal_list.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):
    context = {}
    context['cereal'] = Cereal.objects.get(pk=pk)
    context['number_of_cereals'] = len(context['cereal'].manufacturer.cereal_set.all())
    context['auth'] = request.user.is_authenticated()

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def manufacturer_list(request):
    context = {}
    context['request'] = request
    request.META['HTTP_REFERER'] = '{% url "manufacturer_list" %}'
    form = Search(request.GET)
    context['form'] = form
    context['results'] = None
    context['manufacturers'] = Manufacturer.objects.all().order_by('name')
    if form.is_valid():
        print form.cleaned_data
        search = form.cleaned_data['search']
        if len(search) is 0:
            context['manufacturers'] = Manufacturer.objects.all().order_by('name')
            context['results'] = ""
            # redirect('manufacturer_list', kwargs={'anchor': '#search'})
        else:
            context['manufacturers'] = Manufacturer.objects.filter(name__icontains=search).order_by('name')
            if len(context['manufacturers']) is 0:
                context['results'] = "Sorry, no results found!"
            else:
                context['results'] = "Search results: "
            # redirect('manufacturer_list', kwargs={'anchor': '#search'})


        
            

    return render_to_response('manufacturer_list.html', context, context_instance=RequestContext(request))


def manufacturer_detail(request, pk):
    context = {}
    context['manufacturer'] = Manufacturer.objects.get(pk=pk)
    context['number_of_cereals'] = len(context['manufacturer'].cereal_set.all())
    context['request'] = request

    return render_to_response('manufacturer_detail.html', context, context_instance=RequestContext(request))


def create_cereal(request):
    context = {}
    
    context['request'] = request
    form = CreateCerealForm(request.POST or None)
    context['form'] = form
    if (request.method == "POST"):
        if form.is_valid():
            new_cereal = form.save()
            return redirect('cereal_detail', pk=new_cereal.pk)
    return render_to_response('create_cereal.html', context, context_instance=RequestContext(request))


def update_cereal(request, pk):
    context = {}
    context['request'] = request
    cereal = Cereal.objects.get(pk=pk)

    form = UpdateCerealForm(request.POST or None, instance=cereal)
    context['cereal'] = cereal
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('cereal_detail', cereal.pk)

    return render_to_response('update_cereal.html', context, context_instance=RequestContext(request))


def cereal_delete(request, pk=None):
    context = {}
    cereal = Cereal.objects.get(pk=pk)
    context['cereal'] = cereal
    print request.user.is_authenticated()
    if (request.method == "POST" and request.user.is_authenticated()):
        cereal.delete()
        return redirect('cereal_list')

    return render_to_response('cereal_delete.html', context, context_instance=RequestContext(request))


def signup(request):
    context = {}
    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            print form.cleaned_data

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank You For Signing Up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                return redirect('cereal_list')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    if request.method == 'GET':
        context['valid'] = "Please Sign Up!"

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_user(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            print form.cleaned_data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    print("User is valid, active and authenticated")
                    next = request.GET.get('next')
                    if next is not None:
                        return redirect(next)
                    else:
                        return redirect('cereal_list')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    if request.method == 'GET':
        pass

    return render_to_response('login.html', context, context_instance=RequestContext(request))


def logout_user(request):
    logout(request)

    next = request.GET.get('next')
    if next is not None:
        return redirect(next)
    else:
        return redirect('home')


def create_manufacturer(request):
    context = {}
    context['request'] = request

    form = CreateManufacturerForm(request.POST or None)
    context['form'] = form
    if (request.method == 'POST'):
        print 'POST!'
        if form.is_valid():
            new_manufacturer = form.save()
            return redirect('manufacturer_detail', pk=new_manufacturer.pk)
        
    return render_to_response('create_manufacturer.html', context, context_instance=RequestContext(request))


    
    context['request'] = request
    form = CreateCerealForm(request.POST or None)
    context['form'] = form
    if (request.method == "POST"):
        if form.is_valid():
            new_cereal = form.save()
            return redirect('cereal_detail', pk=new_cereal.pk)
    return render_to_response('create_cereal.html', context, context_instance=RequestContext(request))


def manufacturer_delete(request, pk):
    context = {}
    manufacturer = Manufacturer.objects.get(pk=pk)
    context['manufacturer'] = manufacturer
    context['request'] = request

    if request.method == 'POST':
        for cereal in manufacturer.cereal_set.all():
            cereal.manufacturer = None
            cereal.save()

        manufacturer.delete()
        return redirect('manufacturer_list')

    return render_to_response('manufacturer_delete.html', context, context_instance=RequestContext(request))


def contact(request):
    context = {}

    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail("Cereals: %s" % name, message, email, [settings.EMAIL_HOST_USER], fail_silently=False)
        return redirect('feedback')

    return render_to_response('contact.html', context, context_instance=RequestContext(request))

def feedback(request):
    return render(request, 'feedback.html')


def home(request):
    return render(request, 'home.html')


def template_view(request):

    context = {}

    states = Cereal.objects.all()

    context['states'] = states

    return render(request, 'base.html', context)
