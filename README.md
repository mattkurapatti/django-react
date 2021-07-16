# django-react: Movie Search Website

Begin by cloning the repository (you may need to install git):

```bash
git clone https://github.com/mattkurapatti/django-react.git
```

Ensure you have the python 3.0 or greater installed. Install virtual environment if needed:
```bash
pip install virtualenv
```
Navigate to the root directory (..\django-react)

Activate the virtual environment
```bash
venv\Scripts\activate
```

You may need to launch it yourself first with:
```bash
virtualenv env
```

Install dependencies with
```bash
pip install -r requirements.txt
```

Create the MySQL database with:
```bash
python manage.py migrate
```

Now, populate the MySQL Database by running the following scripts (in order):
```bash
manage.py shell < movies\scripts\movies_metadata_to_mysql.py
```
```bash
manage.py shell < movies\scripts\keywords_to_mysql.py
```
Note: the 2nd script may take 30-45 minutes. Additionally, be sure to use the excel files in the github as I had to pre-process some of the data (the JSON in the original dataset wasn't valid)

Run the server:
```bash
python manage.py migrate
```

