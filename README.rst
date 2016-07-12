Video Village for Spartanburg
==============================

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

Getting Started
----------------

- Fork this repository from https://github.com/hub-ology/video_village
- Install Python 3.5+ from https://www.python.org/downloads/ (if you don't already have it)
- In your project directory, set up a new virtual environment for your work:

.. code-block:: bash

	pyvenv venv

- activate the virtual environment

.. code-block:: bash

	source venv/bin/activate

- install the project requirements into the virtual environment:

.. code-block:: bash

    pip install --upgrade pip
	pip install -r requirements/local.txt

- run the project's migrations to get a local sqlite database established:

.. code-block:: bash

	python manage.py migrate

- Create an administrative user for local use and development:

.. code-block:: bash

	python manage.py createsuperuser

- run a server to begin working with the project locally at http://localhost:8000 :

.. code-block:: bash

	python manage.py runserver

Before submitting a pull request, please ensure tests pass locally.
Also add new tests when incorporating new functionality or changing existing behavior.

.. code-block:: bash

	python manage.py test

License
-------
MIT
See LICENSE_ for details.

.. _LICENSE: LICENSE

