# Online Book Store

## Description

The Online Book Store is a Django-based web application where users can view, review, and manage books. It features user authentication, book management, and review functionality. The application uses Django Rest Framework (DRF) for the API, includes JWT authentication for secure login, and supports pagination for review listings.

## Features

- **User Registration and Login**: Users can register and log in using JWT authentication.
- **Book Management**: Admins can manage books via the Django admin panel or shell.
- **Book Listing and Details**: Users can view a list of available books and their details.
- **Review Management**: Users can create and view reviews for books.
- **Pagination**: Reviews are paginated with customizable page sizes.
- **Average Rating**: The average rating for each book is calculated and provided in the review list.

## Prerequisites

- Python 3.8 or later
- Django 4.x
- Django Rest Framework
- Django Simple JWT
- Docker and Docker Compose (optional)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/essam5/online-book-store.git
   cd online-book-store
   ```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Set Up the Database

```bash
python manage.py migrate
```

## Create a Superuser

```bash
python manage.py createsuperuser
```

## Start the Django Development Server

```bash
python manage.py runserver
```

## Using Docker

1. **Build the Docker Image**

```bash
docker build -t online-book-store .
```

2. **Run the Docker Container**

```bash
docker-compose up -d
```

3. **Access the Application**
   - The application will be accessible at http://localhost:8000.

## Testing

1. **Run unit tests**

```bash
python manage.py test
```

2. **OR Run Tests with Docker**

```bash
docker-compose run web python manage.py test
```

## CI/CD
The application uses GitHub Actions for CI/CD. Ensure your pipelines are configured to run tests and lint code and deploy the application as needed.
