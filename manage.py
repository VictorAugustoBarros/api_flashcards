#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sentry_sdk

sentry_sdk.init(
    "https://baf2dd1297b641038527328669da1133@o1007602.ingest.sentry.io/5976397",
    traces_sample_rate=1.0
)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Flashcards.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
