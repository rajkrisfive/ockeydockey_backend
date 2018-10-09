# ockydocky_frontend

> Backend end for ocky_docky

## Build Setup

``` bash
# clone the repo
git clone

# create virtualenv
virtualenv -p python3 env

# activate the env
source path/to/env/bin/activate

# navigate to root folder and install dependencies, make sure vitualenv is activated 
# as shown in previous step
pip install -r requirements.txt

# run migrations
python manage.py migrate

# create superuser, use it to login to admin dashboard
python manage.py createsuperuser

# run fixtures to load default data
python manage.py loadddata category
python manage.py loaddata products
python manage.py loaddata sub_category

# run the server, in port 8000
python manage.py runserver 
```

## API Details
###Sub Category
 http://localhost:8000/products/sub-category-list/
 
### Category API
http://localhost:8000/products/category-list/

### Product API
http://localhost:8000/products/product-list-create/

######Check the above API's in the browser to check out the filter and ordering options.  

