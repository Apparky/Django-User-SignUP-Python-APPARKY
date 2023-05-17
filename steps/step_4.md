## Step 4:

Previously we discuss setting up the `application` and the `HTML`, here w will discuss the `jinga` technique to set up `.css`, `.js` and other files with `.html`


Replace all `.css`, `.js` and other file location like this command billow

```commandline
"{% static 'js/jquery.min.js' %}"
```

```commandline
"{% static '/css/style.css' %}"
```

Before replacing that make sure in the `static` folder you have created the necessary sub folder 

In this case `css` and `js` are the sub folders

Now run the `server` and you'll see the Site will appear at [http://localhost:8000/](http://localhost:8000/), try the system.

Before running the `server` you need to migrate the project so that the database and of its credentials are ready to store the Feedback info.
To migrate copy the following command to your `terminal`.
```commndline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

We are all done. The `server` is ready to fire.
