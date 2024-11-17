import os
import sys

def main():
    # Get DJANGO_ENV environment variable or raise an error if not set
    DJANGO_ENV = os.getenv('DJANGO_ENV')
    if not DJANGO_ENV:
        raise RuntimeError(
            "DJANGO_ENV is not set. Please set it to 'dev', 'staging', or 'prod' in your environment."
        )

    # Dynamically set the settings module based on DJANGO_ENV
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"fund_finder.settings.{DJANGO_ENV}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your "
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
