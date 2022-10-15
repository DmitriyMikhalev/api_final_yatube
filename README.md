# YaTube API

This app is REST API according to YaTube project. Opportunities for interaction with posts, comments and groups are provided. Authorization is provided by JsonWebToken.

## Installation
Clone the project into your local repository:
```bash
git clone <url>
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:
```bash
pip install -r requirements.txt
```
Now you have to apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
And then run the server:
```bash
python manage.py runserver
```
## Usage
Example request:
```bash
GET http://127.0.0.1:8000/api/v1/posts/{id}/
```
Example response:
```python
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
All endpoints and examples are in the documentation:
```
GET http://127.0.0.1:8000/redoc/
```
