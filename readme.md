                       _    _                   ______  _              _    ______         _  _                     _         _
                      | |  | |                  |  ___|| |            | |   | ___ \       (_)| |                   | |       | |
         _ __   _   _ | |_ | |__    ___   _ __  | |_   | |  __ _  ___ | | __| |_/ /  ___   _ | |  ___  _ __  _ __  | |  __ _ | |_   ___
        | '_ \ | | | || __|| '_ \  / _ \ | '_ \ |  _|  | | / _` |/ __|| |/ /| ___ \ / _ \ | || | / _ \| '__|| '_ \ | | / _` || __| / _ \
        | |_) || |_| || |_ | | | || (_) || | | || |    | || (_| |\__ \|   < | |_/ /| (_) || || ||  __/| |   | |_) || || (_| || |_ |  __/
        | .__/  \__, | \__||_| |_| \___/ |_| |_|\_|    |_| \__,_||___/|_|\_\\____/  \___/ |_||_| \___||_|   | .__/ |_| \__,_| \__| \___|
        | |      __/ |                                                                                      | |
        |_|     |___/                                                                                       |_|


## What?

- Code structure for a normal python flask application

  Includes:

  - One blueprint route - `/`
  - Templates
  - Model class with mysql python migrate


## Setup

```
cd <pathToFolder>/pythonFlaskBoilerplate
virtualenv venv
pip install -r requirements.lock
python run.py
```

## Useful commands

- `flask db migrate`
- `flask db upgrade`


## Refs:

- [Flask Quickstart Guide](flask.pocoo.org/docs/0.11/quickstart/)
- [Jinja2 Templating Engine](http://jinja.pocoo.org/docs/dev/)
- [Flask SqlAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/)
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Contact for TODOs, Imporovemtns etc..

- Add a new issue [here](https://github.com/jitendra-1217/pythonFlaskBoilerplate/issues/new)
- jitendraojha1217@gmail.com
