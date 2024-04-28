from setuptools import setup, find_packages

setup(
    name='django-dictionary-widget',
    version='0.1.0',
    packages=[
        'django_dictionary_widget',
    ],
    include_package_data=True,
    license='MIT',
    description='Django dictionary widget for jsonfield',
    long_description=open('README.md').read(),
    url='https://github.com/kakaKaeng/django-dictionary-widget',
    author='Pattarapong Tantikovit',
    author_email='your@email.com',
    keywords='django-dictionary-widget',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
