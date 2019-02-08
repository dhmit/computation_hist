# Unboxing Django

Getting django up and running requires a few unboxing steps.


#### Install the required python packages
Open a terminal in the computation_hist main directory. In PyCharm, you can just click on "Terminal" 
on the bottom left side. 
You know you're in the right directory if running `ls` returns (among others) `requirements.txt` and 
`setup.py`.

#### Move to django directory and apply migrations
```
cd djweb
python ./manage.py migrate
```

#### Create a super user to access the admin interface
```
python ./manage.py createsuperuser
```

#### Run the development server
```
python ./manage.py runserver
```

Now, you can access either the website itself at [http://127.0.0.1:8000/dj_comp_hist/](http://127.0.0.1:8000/dj_comp_hist/).

Or you can go into the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

###How To Populate Database With Metadata
If you have not migrated yet, do that first.
####Begin by running the server.
```
python manage.py shell
```
####Import a file located in dj_comp_hist.
```
from dj_comp_hist import models
```
####From the models that we just imported, import the function populate_from_metadata.
```
from dj_comp_hist.models import populate_from_metadata
```
####Now it's time to use the function!
Unless you are populating from a metadata that is different from metadata.csv, do not pass in a 
parameter (the function will assume the path to metadata.csv as default)
```
populate_from_metadata()
```