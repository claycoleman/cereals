from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from mmain.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mmain.forms import UserSignUp, UserLogin, Search
from django import forms


def cereal_list(request):
    context = {}
    context['request'] = request
    context['cereals'] = Cereal.objects.all().order_by('name')
    print request.user
    form = Search(request.GET)
    if form.is_valid():
        print form.cleaned_data
        search = form.cleaned_data['search']
        context['cereals'] = Cereal.objects.filter(name__istartswith=search).order_by('name')
        if search is None:
            context['cereals'] = Cereal.objects.all().order_by('name')
    context['length'] = len(context['cereals'])
    context['form'] = form

    return render_to_response('cereal_list.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):
    context = {}
    context['cereal'] = Cereal.objects.get(pk=pk)
    context['auth'] = request.user.is_authenticated()

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def manufacturer_list(request):
    context = {}
    context['request'] = request
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
        else:
            context['manufacturers'] = Manufacturer.objects.filter(name__istartswith=search).order_by('name')
            if len(context['manufacturers']) is 0:
                context['results'] = "Sorry, no results found!"
            else:
                context['results'] = "Search results: "
        
            

    return render_to_response('manufacturer_list.html', context, context_instance=RequestContext(request))


def manufacturer_detail(request, pk):
    context = {}
    context['manufacturer'] = Manufacturer.objects.get(pk=pk)
    context['request'] = request

    return render_to_response('manufacturer_detail.html', context, context_instance=RequestContext(request))


def create_cereal(request, pk=None):
    context = {}
    context['cereal'] = None
    if pk != None: 
        context['cereal'] = Cereal.objects.get(pk=pk)
    context['request'] = request
    context['manufacturers'] = Manufacturer.objects.all()

    if (request.method == 'POST'):
        print 'POST!'
        new_cereal, created = Cereal.objects.get_or_create(name=request.POST.get('name', None))
        new_cereal.cereal_type = request.POST.get('cereal_type', None)
        new_cereal.calories = request.POST.get('calories', None)
        new_cereal.protein = request.POST.get('protein', None)
        new_cereal.fat = request.POST.get('fat', None)
        new_cereal.sodium = request.POST.get('sodium', None)
        new_cereal.dietary_fiber = request.POST.get('dietary_fiber', None)
        new_cereal.carbs = request.POST.get('carbs', None)
        new_cereal.sugars = request.POST.get('sugars', None)
        new_cereal.display_shelf = request.POST.get('display_shelf', None)
        new_cereal.potassium = request.POST.get('potassium', None)
        new_cereal.vitamins_and_minerals = request.POST.get('vitamins_and_minerals', None)
        new_cereal.serving_size_weight = request.POST.get('serving_size_weight', None)
        new_cereal.cups_per_serving = request.POST.get('cups_per_serving', None)

        manu = Manufacturer.objects.get(pk=request.POST.get('manufacturer', None))
        new_cereal.manufacturer = manu

        new_cereal.save()
        manu.save()
        return redirect('cereal_detail', pk=new_cereal.pk) 

    elif (request.method == 'GET'):
        print "Skipped bc GET"

    return render_to_response('create_cereal.html', context, context_instance=RequestContext(request))


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

    return redirect("cereal_list")


def create_manufacturer(request, pk=None):
    context = {}
    context['manufacturer'] = None
    cereals  = Cereal.objects.all()
    if pk != None: 
        manufacturer = Manufacturer.objects.get(pk=pk)
        for cereal in manufacturer.cereal_set.all():
            cereals = cereals.exclude(pk=cereal.pk)

        context['manufacturer'] = manufacturer
    context['request'] = request
    context['cereals'] = cereals

    if (request.method == 'POST'):
        print 'POST!'
        new_manufacturer, created = Manufacturer.objects.get_or_create(name=request.POST.get('name', None))
        cereal_pk_list = request.POST.getlist("cereals")
        print cereal_pk_list
        for pk in cereal_pk_list:
            cereal = Cereal.objects.get(pk=pk)
            cereal.manufacturer = new_manufacturer
            cereal.save()
        new_manufacturer.save()
        return redirect('/manufacturer_detail/'+str(new_manufacturer.pk) )

    return render_to_response('create_manufacturer.html', context, context_instance=RequestContext(request))


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

def template_view(request):

    context = {}

    states = Cereal.objects.all()

    context['states'] = states

    return render(request, 'base.html', context)
