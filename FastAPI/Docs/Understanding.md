# FastAPI

## 09/09/2026

# What is an API?

**API (Application Programming Interface)** is a mechanism that allows two software components to communicate with each other using a defined set of:

* Rules
* Protocols
* Data formats

APIs commonly follow a **request-response** model.

```text
Client
   ↓
 HTTP Request
   ↓
  API
   ↓
Backend / Application
   ↓
 HTTP Response
   ↓
Client
```

---

# Why Do We Need APIs?

Suppose an application has a database containing sensitive information.

We generally **do not want external applications to directly access the database** because this can create security and data-management problems.

Instead, we expose specific functionality through a backend API.

```text
External Application
        ↓
       API
        ↓
    Backend
        ↓
    Database
```

The API acts as a controlled layer between the external application and the database.

### Without an API

```text
External Application
        ↓
    Direct Database Access
```

This can expose the database unnecessarily.

### With an API

```text
External Application
        ↓
       API
        ↓
    Backend
        ↓
    Database
```

The backend can:

* Authenticate users
* Authorize requests
* Validate input
* Apply business logic
* Control what data can be accessed
* Protect sensitive database operations

---

# Monolithic Architecture

In a **monolithic architecture**, many parts of an application are tightly coupled together.

For example:

```text
┌──────────────────────────────┐
│       Monolithic App         │
│                              │
│  UI + Backend + Business     │
│  Logic + Database Access     │
│                              │
└──────────────────────────────┘
```

If another application needs to interact with the system, we generally expose selected functionality through an API rather than giving it direct access to the database.

---

# What is FastAPI?

**FastAPI** is a modern, high-performance Python web framework for building APIs.

It is designed to make API development:

* Fast to run
* Fast to develop
* Easy to validate
* Easy to document
* Easy to maintain

FastAPI is built on top of two important libraries:

1. **Starlette**
2. **Pydantic**

---

# Starlette

**Starlette** is the web framework/toolkit underneath FastAPI that provides the ASGI-based web functionality.

It handles things such as:

* HTTP requests
* HTTP responses
* Routing
* Middleware
* WebSockets
* Other web-related functionality

Simplified:

```text
HTTP Request
     ↓
 Starlette
     ↓
 FastAPI Application
     ↓
HTTP Response
```

---

# Pydantic

**Pydantic** is used for **data validation and data parsing**.

It checks whether incoming data matches the expected structure and types.

For example, suppose an API expects:

```json
{
    "name": "Pulkit",
    "age": 25
}
```

We can define a data model that expects:

```text
name → string
age  → integer
```

If the client sends:

```json
{
    "name": "Pulkit",
    "age": "hello"
}
```

Pydantic can detect that the data does not match the expected type.

### Simplified Flow

```text
Client Request
      ↓
   Pydantic
      ↓
Validate / Parse Data
      ↓
FastAPI Application
```

---

# Why FastAPI?

The two main ideas are:

```text
FastAPI
   │
   ├── Fast to Run
   │
   └── Fast to Code
```

---

# 1. Fast to Run

FastAPI is designed for high-performance API applications and is based on the **ASGI (Asynchronous Server Gateway Interface)** ecosystem.

A common server used to run FastAPI applications is **Uvicorn**.

---

## Uvicorn

**Uvicorn** is an ASGI web server.

Its job is to receive HTTP requests and communicate with the FastAPI application.

A simplified architecture is:

```text
Client
  ↓
HTTP Request
  ↓
Uvicorn
  ↓
ASGI
  ↓
FastAPI
  ↓
Python Application Code
  ↓
ASGI
  ↓
Uvicorn
  ↓
HTTP Response
  ↓
Client
```

---

# ASGI

**ASGI (Asynchronous Server Gateway Interface)** is a standard interface between:

* Web servers
* Python web applications/frameworks

It allows Python web applications to handle both synchronous and asynchronous operations.

FastAPI uses the ASGI ecosystem.

---

# HTTP Request and Response

An HTTP request contains information such as:

* HTTP method
* URL/path
* Headers
* Query parameters
* Request body

For example:

```http
POST /users
Content-Type: application/json

{
    "name": "Pulkit",
    "age": 25
}
```

The server sends an HTTP response containing information such as:

* Status code
* Headers
* Response body

For example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "User created"
}
```

---

# FastAPI vs Flask

Both **FastAPI** and **Flask** are Python web frameworks that can be used to build APIs.

One important difference is the underlying web interface:

| Framework | Interface          | Asynchronous Support                                                               |
| --------- | ------------------ | ---------------------------------------------------------------------------------- |
| FastAPI   | ASGI               | Excellent                                                                          |
| Flask     | WSGI traditionally | Traditionally synchronous; modern Flask also supports async views with limitations |

---

# WSGI

**WSGI (Web Server Gateway Interface)** is the traditional standard interface between Python web applications and web servers.

Flask was traditionally built around the WSGI ecosystem.

A common WSGI server is **Gunicorn**.

```text
Client
  ↓
Gunicorn
  ↓
WSGI
  ↓
Flask
  ↓
Python Application
```

---

# ASGI vs WSGI

### WSGI

```text
Client
  ↓
Web Server
  ↓
WSGI
  ↓
Python Application
```

Traditionally designed around synchronous request handling.

### ASGI

```text
Client
  ↓
Web Server
  ↓
ASGI
  ↓
Python Application
```

Designed to support asynchronous communication and use cases such as:

* Async HTTP handling
* Long-lived connections
* WebSockets

> **Important:** ASGI is not automatically "faster" for every task. Its major advantage is efficient handling of I/O-bound and asynchronous workloads.

---

# Why is FastAPI Fast to Code?

FastAPI provides several features that reduce development effort.

## 1. Automatic Input Validation

FastAPI uses Python type hints and Pydantic models to validate request data.

```python
def create_user(name: str, age: int):
    ...
```

The expected types are clearly defined.

---

## 2. Automatic API Documentation

FastAPI automatically generates interactive API documentation.

Common documentation endpoints include:

```text
/docs
```

and:

```text
/redoc
```

This makes it easy to:

* Explore API endpoints
* Understand request parameters
* Test APIs
* Understand response formats

---

## 3. Python Type Hints

FastAPI makes extensive use of Python type hints.

For example:

```python
name: str
age: int
email: str
```

This improves:

* Validation
* Documentation
* Developer experience
* Code readability

---

# Client and Server

When software or a website needs to communicate with another system, the systems often follow a **client-server architecture**.

### Client

The **client** is the system that makes a request.

Examples:

* Web browser
* Mobile application
* Desktop application
* Another backend service

### Server

The **server** receives requests, processes them, and sends responses.

```text
Client
  │
  │ HTTP Request
  ↓
Server
  │
  │ HTTP Response
  ↓
Client
```

---

# Same Machine vs Different Machines

Software does not necessarily need to run on different physical machines to use a client-server architecture.

### Same Machine

A client and server can run on the same computer.

```text
Computer
┌─────────────────────────┐
│ Client → Server         │
└─────────────────────────┘
```

For example, during local development:

```text
Browser
   ↓
localhost:8000
   ↓
FastAPI
```

### Different Machines

A client can communicate with a server running on another machine over a network.

```text
Client Computer
      ↓
    Internet
      ↓
Server Computer
      ↓
   Backend
```

---

# Static vs Dynamic Applications

Applications can broadly be thought of as **static** or **dynamic**, although real-world systems can combine both.

## Static Applications / Websites

Static content generally remains the same unless the files are manually changed or redeployed.

Examples:

* Simple informational websites
* Documentation pages
* Personal static blogs

```text
Request
   ↓
Static File
   ↓
Response
```

---

## Dynamic Applications / Websites

Dynamic applications generate or modify content based on:

* User input
* Database data
* Authentication
* Business logic
* Current application state

Examples:

* Instagram
* Online banking
* E-commerce applications
* Social media platforms
* Web applications with user accounts

```text
User Request
     ↓
Backend
     ↓
Business Logic
     ↓
Database
     ↓
Generated Response
     ↓
User
```

---

# CRUD

Many dynamic applications perform four fundamental database/application operations known as **CRUD**.

| CRUD Operation | Meaning |
| -------------- | ------- |
| **C**          | Create  |
| **R**          | Read    |
| **U**          | Update  |
| **D**          | Delete  |

---

# HTTP Methods

HTTP methods describe the intended operation of an HTTP request.

Common methods include:

* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`

A common mapping to CRUD is:

| CRUD   | HTTP Method     | Purpose               |
| ------ | --------------- | --------------------- |
| Create | `POST`          | Create a new resource |
| Read   | `GET`           | Retrieve a resource   |
| Update | `PUT` / `PATCH` | Update a resource     |
| Delete | `DELETE`        | Delete a resource     |

### Example

Suppose we have a `/users` API.

#### Create User

```http
POST /users
```

```json
{
    "name": "Pulkit",
    "age": 25
}
```

#### Get Users

```http
GET /users
```

#### Update User

```http
PUT /users/1
```

or:

```http
PATCH /users/1
```

#### Delete User

```http
DELETE /users/1
```

---

# PUT vs PATCH

Both are used for updates, but they are commonly used differently.

### PUT

Generally used to **replace the complete representation** of a resource.

```http
PUT /users/1
```

```json
{
    "name": "Pulkit",
    "age": 26,
    "city": "Surat"
}
```

### PATCH

Generally used for a **partial update**.

```http
PATCH /users/1
```

```json
{
    "age": 26
}
```

---

# FastAPI Architecture — Simplified

The overall flow can be summarized as:

```text
                    CLIENT
                      │
                      │ HTTP Request
                      ↓
                  UVICORN
                      │
                      ↓
                    ASGI
                      │
                      ↓
                  FASTAPI
                  /       \
                 /         \
          Pydantic        Routes
          Validation         │
                 \           /
                  \         /
                   Python
                Application
                     │
                     ↓
                  Database
                     │
                     ↓
                Application
                     │
                     ↓
                  FastAPI
                     │
                     ↓
                    ASGI
                     │
                     ↓
                  Uvicorn
                     │
                     ↓
                HTTP Response
                     │
                     ↓
                   CLIENT
```

---

# Key Concepts to Remember

| Concept   | Meaning                                                   |
| --------- | --------------------------------------------------------- |
| API       | Interface that allows software components to communicate  |
| HTTP      | Protocol commonly used for web communication              |
| FastAPI   | Python framework for building APIs                        |
| Starlette | Provides FastAPI's underlying web/ASGI functionality      |
| Pydantic  | Data validation and parsing                               |
| Uvicorn   | ASGI web server commonly used with FastAPI                |
| ASGI      | Interface supporting asynchronous Python web applications |
| WSGI      | Traditional synchronous Python web interface              |
| Client    | System that sends a request                               |
| Server    | System that receives and processes requests               |
| CRUD      | Create, Read, Update, Delete                              |
| GET       | Retrieve data                                             |
| POST      | Create/submit data                                        |
| PUT       | Replace/update a resource                                 |
| PATCH     | Partially update a resource                               |
| DELETE    | Delete a resource                                         |
