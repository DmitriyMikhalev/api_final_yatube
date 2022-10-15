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
## Endpoints
Tokens:
- .../api/v1/jwt/create/ - create token (POST)
- .../api/v1/jwt/refresh/ - refresh token (POST)
- .../api/v1/jwt/verify/ - check token validity (POST)

Each of the above resources must be requested with the transfer of authorization data via username and password

Posts:
- .../api/v1/posts/ - list of posts (GET) or create post(POST, only for authorized)
- .../api/v1/posts/{id}/ - post object (GET, PUT, PATCH, DELETE). Only the author has access to editing.

Comments:
- .../api/v1/posts/{post_id}/comments/ - list of comments (GET) or create comment (POST, only for authorized)
- .../api/v1/posts/{post_id}/comments/{id}/ - comment object (GET, PUT, PATCH, DELETE). Only the author has access to editing.

Groups:
- .../api/v1/groups/ - list of groups (GET)
- .../api/v1/groups/{id}/ - group object (GET)

Follow:
- .../api/v1/follow/ - list of follows (GET) or create follow (POST, only for authorized)



Examples and required payload are in the documentation:
```
GET http://127.0.0.1:8000/redoc/
```
