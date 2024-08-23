

# Django Database Selector

This Django app allows developers to easily specify which database to use for an entire request process or specific functions by adding annotations like `@using_db("write_db")` or `@using_db("read_db")`. The specified database is then used throughout the request handling process or for the annotated function.

## Features

- **Easy Database Selection**: Specify the database for a request or function using simple annotations.
- **Request-Scoped Database Usage**: The selected database is used consistently across the entire request process.
- **Function-Scoped Database Usage**: Annotate specific functions to ensure their database operations use a specified database.
- **Automatic Routing for GET Requests**: GET requests can be automatically routed to a read/replica database.
- **Support for Multiple Databases**: Works seamlessly with Django's multiple database setup.
- **Context Management with contextvars**: Internally, the app uses [contextvars](https://docs.python.org/3/library/contextvars.html) to ensure the correct database is used within the appropriate scope.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kasv-p/db-router-python.git
   cd db-router-python
   ```

2. **Install the required dependencies:**

   Make sure you have Django installed in your environment. If not, you can install it using pip:

   ```bash
   pip install django
   ```

   Install the app:

   ```bash
   python setup.py install
   ```

3. **Add the app to your Django project:**

   In your Django project's `settings.py`, add the app to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       # Other apps
       'StoreFront',
   ]
   ```

4. **Configure your databases:**

   In your Django project's `settings.py`, define your databases:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3'
       },
       'read_db': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'read_db.sqlite3'
       },
       'write_db': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'write_db.sqlite3'
       }
   }
   ```

## Usage

### Request-Based Database Selection

1. **Annotate your views:**

   Use the `@using_db` annotation to specify which database to use for a particular view:

   ```python
   @using_db("write_db")
   def add_item(request):
       serializer = ItemSerializer(data=request.data)
       if serializer.is_valid():
           item = serializer.save()
           return HttpResponse(item, status=status.HTTP_201_CREATED)
       return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   ```

2. **Automatic Routing for GET Requests:**

   By default, all GET requests can be routed to a read/replica database:

   ```python
   @api_view(['GET'])
   @using_db("read_db")
   @require_http_methods(["GET"])
   def get_item(request, item_id):
       return HttpResponse(get_object_or_404(Item, id=item_id))
   ```

### Function-Based Database Selection

You can also annotate specific functions to use a designated database, regardless of the request context:

```python
@using_db("write_db")
def perform_secondary_db_operation():
    MyModel.objects.create(name="Example")
```

## Contact

For any inquiries or issues, please contact [ksvd1234@gmail.com](mailto:ksvd1234@gmail.com).
