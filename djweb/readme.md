# Unboxing Django

Getting django up and running requires a few unboxing steps.


#### Install the required python packages
Open a terminal in the computation_hist main directory. In PyCharm, you can just click on "Terminal" 
on the bottom left side. 
You know you're in the right directory if running `ls` returns (among others) `requirements.txt` and 
`setup.py`.

Then run:
```
pip install -r requirements.txt
```

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