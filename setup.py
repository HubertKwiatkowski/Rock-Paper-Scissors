try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A rocks-paper-scissors game',
    'author': 'Hubert Kwiatkowski',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'aothor_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts:' [],
    'name': 'Rock-Paper-Scissors'
}

setup(**config)
