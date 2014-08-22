Schedule/badge management site for during Electromagnetic Field camp.

Starting
========
```
sudo apt-get install python-virtualenv python-dev sqlite3 libffi-dev
make init
make update
make data
```

For live (or if you prefer):
```
sudo apt-get install postgresql postgresql-server-dev-9.1 libffi-dev
pip install psycopg2
```

Running
=======
```
make update
make db
make
```

Links to Documentation
======================

## Flask

* [Flask](http://flask.pocoo.org/docs/)
* [Flask-Script](http://packages.python.org/Flask-Script/)

## Templates

* [Jinja2](http://jinja.pocoo.org/docs/)
* [Bootstrap](http://twitter.github.com/bootstrap/)

## Forms

* [Flask-WTF](http://packages.python.org/Flask-WTF/)
* [WTForms](http://wtforms.simplecodes.com/docs/1.0.1/)

## Database

* [Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy/)

