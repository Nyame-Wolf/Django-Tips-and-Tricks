# Using a custom user model when starting a project
>If you’re starting a new project, it’s highly recommended to set up a custom user model, 
>even if the default User model is sufficient for you. This model behaves identically to the default user model, but you’ll be
able to customize it in the future if the need arises:

    from django.contrib.auth.models import AbstractUser

       class User(AbstractUser):
        pass
    
>Don’t forget to point **AUTH_USER_MODEL**  to it in the **settings.py**. Do this before creating any migrations or running
>manage.py migrate for the first time.

    AUTH_USER_MODEL = 'myapp.MyUser'


>Also, register the model in the app’s admin.py:

    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User
    
    admin.site.register(User, UserAdmin)
    
>Don’t forget to point AUTH_USER_MODEL to it. 
>Do this before creating any migrations or running manage.py migrate for the first time.

https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
