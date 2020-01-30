from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'account/home.html')


def register(request):
    if request.method == 'POST':
        # request.POST adds data from our forms
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # Validates to see if the data given is valid
            form.save()  # saves a new user to database
            username = form.cleaned_data.get(
                'username')  # Retrieves the saved user's
            # returns a flash message to inform us a user has been added
            messages.success(
                request, f'Account for {username} created. PLease Login')
            return redirect('login')  # Redirects new user to login page
    else:
        form = CustomUserCreationForm()  # renders an empty form
    return render(request, 'account/register.html', {'form': form})
