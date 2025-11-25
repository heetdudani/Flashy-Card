import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_awesome_project.settings')

application = get_wsgi_application()
app = application  # <--- Add this line specifically for Vercel [cite: 23]
