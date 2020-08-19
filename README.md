# drf-image-gallery-search

Image gallery search based on Django REST Framework.

[![Build Status](https://travis-ci.org/Hephest/drf-image-gallery-search.svg?branch=master)](https://travis-ci.org/Hephest/drf-image-gallery-search)
![GitHub last commit](https://img.shields.io/github/last-commit/Hephest/drf-image-gallery-search)
[![Updates](https://pyup.io/repos/github/Hephest/drf-image-gallery-search/shield.svg)](https://pyup.io/repos/github/Hephest/drf-image-gallery-search/)
[![Python 3](https://pyup.io/repos/github/Hephest/drf-image-gallery-search/python-3-shield.svg)](https://pyup.io/repos/github/Hephest/drf-image-gallery-search/)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Development](#development)
- [TODO List](#todo-list)

## Features

- Django 3.0+
- Django REST Framework 3.11+
- PostgreSQL 12.3+
- Fully dockerized, local development via `docker-compose`
- Caching support via `Redis` and `Celery`
- Travis CI support
- Testing with `coverage` and `nose` test runner
- Dependencies and security updates enforced by [pyup.io](https://pyup.io/)
- Linting tools support (`isort`, `flake8`)

## Getting Started

### Prerequisites

Project based on Docker containers. As basic prerequisites, you need to get:

- **Docker v.19.03.11-ce** (Linux) or **Docker Machine** (Windows, MacOS)
- **Docker Compose v.1.26.0**

### Installing

Clone repository to your local machine:

    git clone https://github.com/Hephest/drf-image-gallery-search.git

Create and fill .env file (example below):

    # Django
    DJANGO_SECRET_KEY = 'h*3-=2ts1zznjts4rl+4ehakk7p3ncdh-jevt3y03h9ze(+3a7'
    
    # PostgreSQL
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_HOST = 'db'
    DB_PORT = 5432

Run docker-compose:

    docker-compose up

### Development

1. Set up virtual environment via provided `requirements.txt`
    
        python -m venv venv/
        source venv/bin/activate
        pip install -r requirements.txt
        
2. Write code and tests accordingly to your pipeline or development technology (TDD, DDD etc.)
3. Run tests via `docker-compose`:

        docker-compose run web python manage.py makemigrations
        docker-compose run web python manage.py migrate
        docker-compose run web python manage.py test
        
4. Before `git commit`, make sure to check your code with `isort` and `flake8` manually:

        isort
        flake8
        
5. After `git push`, check Travis CI build for possible errors

## TODO List

- [ ] Celery task for receiving pictures
- [ ] `/search/` API endpoint
- [x] Redis as default cache backend