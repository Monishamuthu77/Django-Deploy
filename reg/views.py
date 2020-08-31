from django.shortcuts import render, redirect
from .forms import Register
from .models import RegisterModel


# Create your views here.
def home(request):
    image = RegisterModel.objects.last()

    if request.method =="POST":
        form = Register(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            context = {'img': image, 'form': form}
            #return redirect('submit')


        else:
            my_forms = {'my_forms': form}
            return render(request, "index.html", my_forms)

    else:
        form =Register()
    my_forms = {'my_forms' : form}

    return render(request, "index.html", my_forms)