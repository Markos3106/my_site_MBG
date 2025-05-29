import os
import django
import pydoc

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
django.setup()

# Genera documentació dels mòduls
pydoc.writedoc('blog.models')
pydoc.writedoc('blog.views')
pydoc.writedoc('blog.tests')