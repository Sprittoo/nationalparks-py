"""Application entry point: starts the Flask app with Gunicorn."""
import os
import sys

if __name__ == '__main__':
    # Run gunicorn with options equivalent to the previous mod_wsgi setup
    bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
    args = [
        sys.executable, '-m', 'gunicorn',
        '--bind', bind,
        '--access-logfile', '-',
        '--error-logfile', '-',
        '--capture-output',
        '--enable-stdio-inheritance',
        '--timeout', '60',
        '--workers', '1',
        '--forwarded-allow-ips', '*',  # trust X-Forwarded-* from proxy (OpenShift)
        'wsgi:application',
    ]
    os.execv(sys.executable, args)
