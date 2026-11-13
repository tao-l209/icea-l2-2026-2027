"""
ASGI config for galerie_projet project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< Updated upstream
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "galerie_projet.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galerie_projet.settings')
>>>>>>> Stashed changes

application = get_asgi_application()
