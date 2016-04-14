django-exception-blame
======================

A django middleware for exception blaming

## Overview

Basically it looks in the exception traceback and search for the line number of the first file of your reopsitory that raised the exception. It uses git to blame the author of that file and line number, then adds the info to the request metadata.

Only for use with `DEBUG=True`

## Installation

Install using `pip`

    pip install django-exception-blame

## Configuration

Add the following to your `settings.py` module:

Add the middleware to your `MIDDLEWARE_CLASSES` setting

    MIDDLEWARE_CLASSES = [
        ...
        'exceptionblame.middleware.ExceptionBlameMiddleware',
    ]

Configure the repository root.

    EXCEPTION_BLAME = {
        'REPO_DIR': '/your/repository/dir'
    }

## License

This project is licensed under the MIT License - see the `LICENSE` file for details


