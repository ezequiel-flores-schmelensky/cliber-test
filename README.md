# Cliber Test

This a test for a job offer

## Tools 🛠️

- Visual Studio Code

## Tasks 📋


_Menciona las herramientas que utilizaste para crear tu proyecto_

Using the [API of GitHub](https://docs.github.com/en/free-pro-team@latest/rest/reference) do the following tasks:

- Create a script called `[seed.py](http://seed.py)` that populates a SQLite database. By default it should search for the first 150 users from GitHub but the script should accept a param called `total` to customize the number of users.
- The fields required for this users are:
    - username
    - id
    - image url
    - type
    - link to his GitHub profile

Once you have created the script and has a complete db create a Flask application that has:

- A view to show the info of all the users of the database in a table. Profile avatar should be visible and clicking the username should send me to the GitHub profile. Pagination is needed and by default it should be of size 25. Make sure that the page is responsive even with a large amount of data (use any optimization) *Optional but desired*: arguments to change pagination size and ordering

Create an script to run your server and a `README.md` file where you explain your decisions and architecture.

Unit tests for all the code is needed.

After completion of the tasks create a public repository and put all the code there. Be sure to not include compiled files and the db.

Optional

- Add an endpoint where you return a JSON with the information stored in the database. The user will be able to use query params to filter the results. At least there should be for username and id but for type, pagination size, order by and GitHub profile is a plus. Example:

`<your_endpoint>/profiles?username=test1&pagination=20&order_by=id`


## Architecture 🔧

The architecture was made in that way because it was a simple test and to join both tasks (seed.py and flask), personally, I prefer to work with Django framework which is easier from point of view; an app directory was created to store models and views to have better control of them, furthermore, some code in the __init__.py files was added to have faster access to the classes.

The "templates" directory was located at the same level as the app directory to identify the HTML files faster, as well as static directory and settings, the last one mentioned could be modified to work with production or develop variables.

Finally, this architecture helped me to implement the API endpoints easily.


## Running Instructions 📦
_Requirements_

```
pip install -r requirements.txt
```

_Seed_

```
python seed.py
```

_Flask_

```
python run.py
```
url to test
http://127.0.0.1:5000//page/<int:page>

_API_

url to test
http://127.0.0.1:5000/api/user/<int:page>/profiles?username=mo&pagination=20&order_by=id


---
⌨️ por [Ezequiel Flores Schmelensky](https://github.com/supereze?tab=repositories) 😊