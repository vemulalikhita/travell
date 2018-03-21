from django.contrib import messages
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,

)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, redirect

from .forms import TourForm, TouristForm
from .forms import UserLoginForm, UserRegistrationForm
from .models import Tour
from .models import Tourist


def tour_create(request):
    form = TourForm(request.POST or None, request.FILES or None)
    if form.is_valid():
     instance = form.save(commit=False)
     instance.save()
     messages.success(request, "Successfully Created")
     return HttpResponseRedirect(instance.get_absolute_url())

            # if request.method == "POST":
        #first_name = request.POST.get("first_name")
        #content = request.POST.get("content")
        #Tour.objects.create(first_name=first_name)
    context = {
        "form": form,
    }
    return render(request, "tour_form.html", context)
    #return HttpResponse("<h1>Create</h1>")


def tour_detail(request, id=None):
    instance = get_object_or_404(Tour, id=id)
    context = {
       # "title": instance.title,
        "instance": instance,
    }
    return render(request, "tour_detail.html", context)

    #return HttpResponse("<h1>Detail</h1>")


def tour_list(request):
    listplace = Tour.objects.all()


    # queryset = Tour.objects.all()
    context = {
        "queryset": listplace,
        "title": "Tour-list",
    }
    return render(request, "index.html", context)


def tour_update(request, id=None):
    instance = get_object_or_404(Tour, id=id)
    form = TourForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        #print form.cleaned_data.get("first_name")
        instance.save()
        messages.success(request, "Successfully Saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        # "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "tour_form.html", context)

    #return HttpResponse("<h1>Update</h1>")


def tour_delete(request, id=None):
    instance = get_object_or_404(Tour, id=id)
    instance.delete()
    messages.success(request, "deleted")
    return redirect("mysite:Tour-list")
    #return HttpResponseRedirect(instance.get_absolute_url())

            #return HttpResponse("<h1>delete</h1>")
#def index(request):
 #   return HttpResponse("<h1>Travell ste")


def tourist_login(request):
    print(request.user.is_authenticated())   #shows successfully loged in shows in powershell
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect("/mysite/list/")
    return render(request, "tourist_login.html", {"form":form, "title":title})


def tourist_register(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = 'Register'
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)

            login(request, new_user)
            if next:
                return redirect(next)
            return redirect("/mysite/list/")

    context = {
            "form": form,
            "title": title,
     }
    return render(request, "tourist_register.html", context)


def tourist_logout(request):
            logout(request)
            return redirect("/mysite/list/")
            #return render(request, "tourist_login.html", {})
    #return HttpResponse("<h1>Create</h1>")


def tourist_detail(request, id=None):
    instance = get_object_or_404(Tourist, id=id)
    context = {

        "title": "Tourist-Detail",
        "instance": instance,
    }
    return render(request, "tourist_detail.html", context)

    #return HttpResponse("<h1>Detail</h1>")


def tourist_create(request):                #mysite/touristcreate
    form = TouristForm(request.POST or None, request.FILES or None)
    if form.is_valid():
     instance = form.save(commit=False)
     instance.save()
     messages.success(request, "successfully created")

     return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "tourist_form.html", context)
   # return HttpResponse("<h1>create</h1>")


def tourist_list(request):
    touristlist = Tourist.objects.all()
    context = {
        "queryset": touristlist,
        "title": "Tourist-List"
    }
    return render(request, "tourist_list.html", context)


def tourist_update(request, id=None, instancee=None):
    instance = get_object_or_404(Tourist, id=id)
    form = TouristForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "successfully saved")
       # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        
        "form": form,
        "instance": instancee,
    }
    return render(request, "tourist_form.html", context)


def tourist_delete(request, id=None):
    instance = get_object_or_404(Tourist, id=id)
    instance.delete()
    messages.success(request, "successfully deleted")
    return redirect("mysite:tourist_list")
