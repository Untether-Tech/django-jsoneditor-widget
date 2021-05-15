import os

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='django-jsoneditor-widget',
    license='MIT',
    version='0.1.0',
    author='Charanjit Singh',
    author_email='charanjitdotsingh@gmail.com',
    url='https://github.com/Untether-Tech/django-jsoneditor-widget',
    packages=['jsoneditor'],
    package_data={
        'jsoneditor': [
            'static/jsoneditor/*.css',
            'static/jsoneditor/*.js',
            'static/jsoneditor/*.map',
            'static/jsoneditor/img/*.svg',
            'templates/jsoneditor/*.html',
        ],
    },
    description='Django form widget form JSONField',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
)
