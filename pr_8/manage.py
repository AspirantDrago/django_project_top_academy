#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pr_8.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    if '--update_brands' in sys.argv:
        from autos.models import Auto
        
        with open('brands.txt', encoding='utf-8') as f:
            for s in map(str.strip, f.readlines()):
                try:
                    obj = Auto.objects.create(name=s)
                    obj.save()
                except BaseException as e:
                    print(e)


if __name__ == '__main__':
    main()
