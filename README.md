# Expense Tracker API

This is an Expense Tracker API built using Django Rest Framework (DRF). It allows users to perform basic CRUD operations to manage their expenses. The API has been tested using Postman.

## Features

- Add, update, and delete expenses
- View all expenses

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd expense-tracker-api
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   pip install djangorestframework
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The following endpoints are available in the Expense Tracker API:

### Expense Endpoints

- **List Expenses**
  - URL: `/api/expenses/`
  - Method: GET
  - Description: Retrieve a list of all expenses.

- **Create Expense**
  - URL: `/api/expenses/`
  - Method: POST
  - Description: Add a new expense.

- **Retrieve Expense**
  - URL: `/api/expenses/<id>/`
  - Method: GET
  - Description: Get details of a specific expense.

- **Update Expense**
  - URL: `/api/expenses/<id>/`
  - Method: PUT/PATCH
  - Description: Update an existing expense.

- **Delete Expense**
  - URL: `/api/expenses/<id>/`
  - Method: DELETE
  - Description: Delete an expense.

## Testing the API

1. Use [Postman](https://www.postman.com/) or any API client to test the endpoints.
2. Use the provided URL paths to perform CRUD operations.
3. Send data in JSON format for POST and PUT requests.

### Sample JSON for Expense
```json
{
  "title": "Grocery Shopping",
  "amount": 100.50,
  "date": "2025-01-15"
}
```

## Built With

- **Django**: High-level Python Web Framework
- **Django Rest Framework (DRF)**: Toolkit for building Web APIs

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [DRF Documentation](https://www.django-rest-framework.org/)

---

Feel free to extend or modify this project as needed. Happy coding!
