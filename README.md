**Note:** Make sure you have a strong internet connection when installing Django. Without a strong internet connection will throw an error.

#### Step five: Create a Django project

After you have installed Django in your virtual environment, the next step is to create a Django project. Use the below command to create a Django project.

`C:\Users\Username\Desktop\django_project>django-admin startproject my_project`

The above command creates a series of file and folder structures as seen below.

`C:\Users\Username\Desktop\django_project>`

        manage.py
        my_project
        __init.py__
        asgi.py
        settings.py
        urls.py
        wsgi.py
    

#### Step six: Create a Django app

Next, you will navigate to your Django project directory–i.e. my\_project–and create your Django app.

Use the below command to navigate to your Django project directory and create your Django app.

`C:\Users\Username\Desktop\django_project>cd my_project`

`C:\Users\Username\Desktop\django_project\my_project>python manage.py startapp my_app`

#### Step seven: Test installation

In your terminal, type the below commands to test your app installations.

`C:\Users\Username\Desktop\django_project\my_project>python manage.py runserver`

The Django server runs on port 8000, with an IP address 127.0.0.1. Open your browser and enter [http://127.0.0.1:8000.](http://127.0.0.1:8000.) If the image below is displayed on your screen, congratulations! you have successfully created your Django app.

![](https://cdn-images-1.medium.com/max/2000/0*R32a9-Wh5xAdOQOU)

### Part two: App configuration and database setup

In this section, you will be creating a database that will enable users to store and retrieve data.

The `model.py` file in the app directory is where you will create the database tables. But first, configure your app.

Let’s get started.

#### Step one: App configurations

Open your Django project with any code editor of your choice. Next, open the `settings.py` file in the my\_project directory. Scroll down to the INSTALLED APPS section, and add your app name–`my_app`, as seen in the image below.

![](https://cdn-images-1.medium.com/max/2000/0*y1HABs0ImD9u51gD)

#### Step two: Create a database table

Navigate to your app directory in your code editor, open the models.py file and insert the below codes.
