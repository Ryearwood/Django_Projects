from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SignUpForm
from website.models import Record


def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("home")
        else:
            messages.success(request, "Error Logging in, please try again...")
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("home")
        else:
            messages.success(request, "Somethings went wrong... Please Try Again")
            return render(request, "register.html", {"form": form})
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect("home")
    else:
        messages.success(request, "You Must Be Logged In To Delete Records...")
        return redirect("home")
