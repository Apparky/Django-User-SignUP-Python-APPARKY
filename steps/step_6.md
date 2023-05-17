## Step 6:

Now integrate some steps in `HTML` to communicate with the server

- Codes for `signup.html`
```commandline
        {% for message in messages %}
        <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
            <strong> {{message}} </strong>
            <button type="button" class="btn-close" data-bs-dismiss = "alert" aris-label="Close"></button>
        </div>
        {% endfor %}

```

Codes for `login.html`
```commandline
        {% for message in messages %}
        <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
            <strong> {{message}} </strong>
            <button type="button" class="btn-close" data-bs-dismiss = "alert" aris-label="Close"></button>
        </div>
        {% endfor %}
```

You are all set Here Run the server and Check all Functionalities.