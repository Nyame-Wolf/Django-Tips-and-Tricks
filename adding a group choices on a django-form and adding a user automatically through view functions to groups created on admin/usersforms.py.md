**On users/forms.py**

    class UserRegisterForm(UserCreationForm):
        group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2', 'location', 'group']
