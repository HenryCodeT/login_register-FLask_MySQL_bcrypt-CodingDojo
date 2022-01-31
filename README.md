# login_register-FLask_MySQL_bcrypt-CodingDojo
### Python - Flask - MYSQL - flash - flask-bcrypt
### Install packages
* ``` pipenv install PyMySQL flask flask-bcrypt ```
* ``` pipenv shell ```
* ``` python server.py ```
### Flash messages 
* ``` user_model.py ``` creating a ```flash``` message with category
 ```python
 flash('al menos 2 letras para el nombre','regiter')
 ```
 * ```inde.html``` show messages
 ```html 
 {% with messages = get_flashed_messages(category_filter = ["register"]) %}
     {% if messages %}
         {% for message in messages %}
             <div class="form-text bg-danger text-dark p-3">{{message}}</div>
         {% endfor %}
     {% endif %}
{% endwith %}
```
### Regular expressions
* ``` user_model.py ``` Creating global variables 
```python
import re
FIRST_LAST_NAME_REGEX = re.compile(r'^[a-zA-Z]{2}')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]{8}')
```
* Using conditions with regular expressions
```python
if not FIRST_LAST_NAME_REGEX.match(registro['firstname'])
if not EMAIL_REGEX.match(registro['email'])
if not PASSWORD_REGREX.match(registro['password1'])
```
### Bcrypt
```python
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
```
* Encrypting the password
```python
 password_encriptado = bcrypt.generate_password_hash(request.form['password1'])
```
* Comparing 
```python
 bcrypt.check_password_hash( response_query_user.password, request.form['password']):
```

