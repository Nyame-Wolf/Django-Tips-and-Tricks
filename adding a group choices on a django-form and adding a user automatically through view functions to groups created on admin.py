https://stackoverflow.com/questions/57986332/

users/forms.py
class UserRegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'location', 'group']
        
users/views.py
from django.shortcuts import render,redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']        
            group.user_set.add(user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
