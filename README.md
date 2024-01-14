# Song App

This is a simple Django project for Song App

# Setup

## 1. Create a Virtual Environment

### On Unix or MacOS
* Navigate to the root of the folder
```bash
python3 -m venv venv
```
### On Windows
```bash
python -m venv venv
```

## 2. Activate the Virtual Environment

### On Unix or MacOS

```bash
source venv/bin/activate
```

### On Windows
```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Navigate to root of project

```bash
cd ./FavoriteTunes
```

## 5. Create Migrations
```bash
python manage.py makemigrations
```

## 6. Run Migrations
```bash
python manage.py migrate
```

## 7. Run the Project
```bash
python manage.py runserver
```

### Access the application at http://127.0.0.1:8000/.
