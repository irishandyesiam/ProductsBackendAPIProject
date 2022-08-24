# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2*a)ro163r*17p)h*zlfq!ii!eiiu*$hsn@!&l0!-j9==@l8s$'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}