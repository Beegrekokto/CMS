# Content Management System

Content Management System is a simple dynamic web system that we modified over the project given by Rajesh Sir. Here, we added different pages and apps over existing project.

## Added Pages

  - Gallery Page
  - Training Page
  - Career Page
  - About Us Page


### Enhancement in Project

- Sluggify completed to generate unique slug
- Broken links fixed
- Mail issue resolved

### Dependencies


- Django==2.0.3
- django-ckeditor==5.4.0
- django-extensions==2.0.7
- django-js-asset==1.1.0
- django-mptt==0.9.0
- django-tinymce==2.7.0
- python==3.6
- Pillow==5.0.0
- pkg-resources==0.0.0
- python-decouple==3.1
- pytz==2018.3
- six==1.11.0


## Installation Steps
```sh
$ git clone http://192.168.102.202/upakar.paudel/CMS.git
$ Environment Setup
$ cd CMS/
$ pip install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
$ Host address : 127.0.0.1, Port : 8000
```

