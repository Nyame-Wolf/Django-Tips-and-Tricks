->This is just an application. One must first have a project 
on project urls...include account urls.
on project settings, add the account app to INSTALLED_APPS
then add :

# refer to https://docs.djangoproject.com/en/3.0/ref/settings/
# This is to activate a custom user added to our project.
AUTH_USER_MODEL = ('account.CustomUser')

# redirects users to homepage on login instead of django default-to their profile.
# Tells Django which URL to redirect after a successful login if no next parameter is present in the request
LOGIN_REDIRECT_URL = "home"

# this tells django where to redirect a user who tries to access a profile page and is not logged in.
# The URL to redirect the user to log in (for example, views using the login_required decorator)
LOGIN_URL = "login"

# The URL to redirect the user to log out
LOGOUT_URL = 'logout'

******for bootstrap
->pip install crispy forms the add this to project urls:
CRISPY_TEMPLATE_PACK = 'bootstrap4'

****for password reset
->this is so that the email can work By adding line below, we use the terminal as an email address.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

-> Alternatively you can add
# setting up email reset
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Use environment variables to avoid people getting access to our emails
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
->this only works if environment variables are set.

