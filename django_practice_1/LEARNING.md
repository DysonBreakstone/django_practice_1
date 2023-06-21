requirements.txt can be used like Ruby's gemfile, unclear exactly how that works.

## To use ipdb (which is like Ruby's 'pry'), insert the following line:

#### Import ipdb; ipdb.set_trace()

- type c to continue execution of the code (like 'exit' for pry)

#### To install these things, I ran in the console:

pip install django-extensions
pip install ipython
python3 -m pip install "ipdb"

## Python admin dashboard:

Admin dashboard can be used to view, add, and delete database items
On a browser, navigate to localhost:{port}/admin

#### To create username and password:

In the terminal: python3 manage.py createsuperuser
create credentials

#### Then:

- in admin.py within app_name

from .models import ToDoList

admin.site.register(ToDoList)
