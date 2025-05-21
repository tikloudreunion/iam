# Architecture

This document outlines the architecture used to build a REST API using **FastAPI** and **SQLModel** with an Object-Oriented Programming (OOP) approach. The chosen architecture pattern is known as **Controller-Service-Repository (CSR)** or **Service Layer Architecture**.

---

## Project Structure

```plain
iam/
├── app.py               # Entry point
├── config.py            # Configuration settings
├── models/              # Data models
├── controllers/         # Business logic
├── routes/              # Routing and endpoints
├── services/            # Utility functions and database interactions
└── database.py          # Database session management
```

## Architecture Overview

The architecture follows the **Controller-Service-Repository** pattern, which separates the concerns of each layer as follows:

### Controller Layer

* **Purpose:** Handles incoming HTTP requests and returns responses.
* **Implementation:** Uses FastAPI routers to define endpoints and link them to services.
* **Example:** `routes/user_routes.py`

### Service Layer

* **Purpose:** Contains business logic and application functionality.
* **Implementation:** Interacts with the controller and the repository to process data.
* **Example:** `services/user_service.py`

### Repository Layer

* **Purpose:** Manages data persistence and retrieval from the database.
* **Implementation:** Uses SQLModel for database interactions.
* **Example:** `controllers/user_controller.py`

### Models

* **Purpose:** Define data structures and ORM models used throughout the application.
* **Example:** `models/user.py`

### Configuration and Initialization

* **Purpose:** Sets up environment variables and database connections.
* **Example:** `config.py`, `database.py`, `__init__.py`

---

## Advantages

1. **Separation of Concerns:** Isolates business logic, data handling, and routing.
2. **Scalability:** Easily extendable with additional services or models.
3. **Maintainability:** Modular structure simplifies updates and debugging.
4. **Testability:** Individual layers can be tested independently.
5. **Reusability:** Components can be reused across different projects.

---

## Example Flow

1. **Client Request:** Sends a `POST` request to create a new user.
2. **Router:** The request hits the endpoint defined in `user_routes.py`.
3. **Service Layer:** Calls the function to add a new user.
4. **Controller Layer:** Interacts with the database and returns the created user.
5. **Response:** The client receives the created user data as a response.

---

## Conclusion

This OOP structure in FastAPI helps maintain a clean, modular, and scalable application. It divides responsibilities among well-defined components, making the API easy to extend and maintain.
