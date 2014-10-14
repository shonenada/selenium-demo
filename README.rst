Demo of selenium
===============================================================================

Test web app with javascript/css.

Using:

1. `foreman` for process manage.(both development and product env)
2. `Procfile` config for foreman

Init Env::

    $ gem install foreman
    $ npm install -g phontomjs

Run in development Env::

    $ foreman start -f Procfile.dev

Run in product Env::

    $ foreman start

Rereferences:

1. `http://phantomjs.org/ <http://phantomjs.org/>`_
2. `http://theforeman.org/ <http://theforeman.org/>`_
3. `https://github.com/ddollar/foreman <https://github.com/ddollar/foreman>`_
4. `https://devcenter.heroku.com/articles/procfile <https://devcenter.heroku.com/articles/procfile>`_
