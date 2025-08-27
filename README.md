# Movie Review API

This is a Django-based REST API for managing movie reviews. It allows users to create, read, update, and delete reviews for movies. The API is built using Django and Django REST Framework and includes user authentication, filtering, and interactive documentation with Swagger UI.

## Features

- **CRUD Operations for Reviews:** Create, Read, Update, and Delete movie reviews.
- **User Management:** CRUD operations for users with authentication.
- **Permissions:** Only authenticated users can create, update, or delete their own reviews.
- **Filtering and Searching:** Filter reviews by movie title or rating, and search by movie title or review content.
- **Pagination:** Paginated results for review listings.
- **API Documentation:** Interactive API documentation using Swagger UI and ReDoc.

## Technical Requirements

- Python 3.8+
- Django
- Django REST Framework
- `django-filter` for filtering
- `drf-yasg` for Swagger documentation

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd alx_final
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email, and password.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The base URL for the API is `/api/`.

| Endpoint                  | HTTP Method | Description                               |
| ------------------------- | ----------- | ----------------------------------------- |
| `/api/users/`             | `GET`, `POST` | List all users or create a new user.      |
| `/api/reviews/`           | `GET`, `POST` | List all reviews or create a new review.  |
| `/api/reviews/{id}/`      | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, or delete a specific review. |
| `/api-token-auth/`        | `POST`      | Obtain an authentication token.           |
| `/api-auth/login/`        | `POST`      | Log in to the browsable API.              |
| `/swagger/`               | `GET`       | Interactive API documentation (Swagger).  |
| `/redoc/`                 | `GET`       | API documentation (ReDoc).                |

## Authentication

To access protected endpoints (creating, updating, or deleting reviews), you need to authenticate using a token.

1.  **Create a user** by sending a `POST` request to `/api/users/`.
2.  **Obtain a token** by sending a `POST` request to `/api-token-auth/` with the user's `username` and `password`.
    ```bash
    curl -X POST -d "username=<your_username>&password=<your_password>" http://127.0.0.1:8000/api-token-auth/
    ```
3.  Include the token in the `Authorization` header for all subsequent requests to protected endpoints.
    ```
    Authorization: Token <your_token>
    ```

## Testing with Swagger UI

For a more user-friendly testing experience, use the Swagger UI.

1.  **Navigate to the Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
2.  **Authorize:**
    *   Click the "Authorize" button at the top right.
    *   In the "Value" field, enter `Token <your_token>` (including the word "Token" and a space).
    *   Click "Authorize".
3.  **Test the endpoints:** You can now use the interface to make requests to all API endpoints. The authorization token will be automatically included in the headers.

## Deployment

This API can be deployed to platforms like Heroku or PythonAnywhere. Ensure you configure the following for a production environment:

-   Set `DEBUG = False` in `settings.py`.
-   Configure `ALLOWED_HOSTS` with your domain name.
-   Use a production-ready database like PostgreSQL.
-   Set up a static file server.
