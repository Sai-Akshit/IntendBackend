# IntendBackend

IntendBackend is a Django REST API designed for managing email addresses. It provides functionality to create, read, update, and delete email entries through a simple API interface.

## Features

-   Create, Read, Update, and Delete (CRUD) operations for email addresses.
-   Simple and easy-to-use API endpoints.
-   Built with Django and Django REST Framework.

## API Endpoints

The API provides the following endpoints for managing email addresses:

### Email Management

-   **`GET /email/`**: Retrieves a list of all email addresses.
    -   **Response:**
        ```json
        [
            {
                "id": 1,
                "email": "user1@example.com",
                "created_at": "YYYY-MM-DDTHH:MM:SS.ffffffZ"
            },
            {
                "id": 2,
                "email": "user2@example.com",
                "created_at": "YYYY-MM-DDTHH:MM:SS.ffffffZ"
            }
        ]
        ```

-   **`POST /email/`**: Creates a new email address.
    -   **Request Body:**
        ```json
        {
            "email": "newuser@example.com"
        }
        ```
    -   **Response (Success - 201 Created):**
        ```json
        {
            "id": 3,
            "email": "newuser@example.com",
            "created_at": "YYYY-MM-DDTHH:MM:SS.ffffffZ"
        }
        ```
    -   **Response (Error - 400 Bad Request):**
        ```json
        {
            "email": [
                "Enter a valid email address."
            ]
        }
        ```

-   **`PUT /email/`**: Updates an existing email address.
    -   **Request Body:**
        ```json
        {
            "id": 1,
            "email": "updateduser1@example.com"
        }
        ```
    -   **Response (Success - 200 OK):**
        ```json
        {
            "id": 1,
            "email": "updateduser1@example.com",
            "created_at": "YYYY-MM-DDTHH:MM:SS.ffffffZ" 
        }
        ```
    -   **Response (Error - 400 Bad Request):**
        ```json
        {
            "email": [
                "Enter a valid email address."
            ]
        }
        ```
    -   **Note:** Requires the `id` of the email to be updated in the request body.

-   **`DELETE /email/`**: Deletes an existing email address.
    -   **Request Body:**
        ```json
        {
            "id": 1
        }
        ```
    -   **Response (Success - 204 No Content):**
        ```json
        {
            "message": "user1@example.com deleted successfully"
        }
        ```
    -   **Note:** Requires the `id` of the email to be deleted in the request body. The success message shown here is based on the current implementation; a 204 response typically has no body, but the view returns a JSON message.

## Setup and Installation

Follow these steps to set up and run the project locally:

### Prerequisites

-   Python (3.8 or higher recommended)
-   pip (Python package installer)
-   virtualenv (optional, but recommended for isolating project dependencies)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd IntendBackend
    ```
    (Replace `<repository_url>` with the actual URL of this repository)

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Create a `.env` file in the root project directory (alongside `manage.py`). Add the following environment variables:
    ```env
    SECRET_KEY='your_django_secret_key'
    DATABASE_NAME='your_db_name'
    DATABASE_USERNAME='your_db_username'
    DATABASE_PASSWORD='your_db_password'
    DATABASE_HOST='your_db_host'
    DATABASE_PORT='your_db_port' 
    ```
    Replace the placeholder values with your actual database credentials and a strong secret key. For `DATABASE_HOST` and `DATABASE_PORT`, if you are running PostgreSQL locally with default settings, these would typically be `localhost` and `5432` respectively.

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API should now be accessible at `http://127.0.0.1:8000/`.

## Running Tests

To run tests, use the following command:

```bash
python manage.py test
```

Currently, there are no specific tests implemented in `api/tests.py`. You can add your tests there.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

Please make sure to update tests as appropriate.

## License

This project is not currently licensed. Please add a `LICENSE` file if you wish to specify licensing terms.
