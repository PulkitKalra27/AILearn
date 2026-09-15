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

---

## 10/09/2026

# Path Parameters

**Path Parameters** are dynamic segments of a URL path used to identify a specific resource.

They are commonly used when we want to:

* Retrieve a specific resource
* Update a specific resource
* Delete a specific resource

### Example

```http
GET /patients/101
```

Here, `101` is the **path parameter** used to identify a particular patient.

In FastAPI:

```python
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return {"patient_id": patient_id}
```

FastAPI extracts `patient_id` from the URL and validates it according to the declared type.

---

# `Path()`

`Path()` is a FastAPI utility function used to provide **validation rules and metadata** for path parameters.

It helps make path parameters more descriptive, validated, and properly documented.

### Things `Path()` can provide

**Metadata:**

* `title`
* `description`
* `example` / `examples`

**Validation:**

* `gt` → greater than
* `ge` → greater than or equal to
* `lt` → less than
* `le` → less than or equal to
* `min_length`
* `max_length`
* `pattern`

### Example

```python
from fastapi import Path

@app.get("/patients/{patient_id}")
def get_patient(
    patient_id: int = Path(
        title="Patient ID",
        description="The unique ID of the patient",
        gt=0
    )
):
    return {"patient_id": patient_id}
```

Here:

```python
gt=0
```

means that the `patient_id` must be greater than `0`.

---

# HTTP Status Codes

**HTTP Status Codes** are three-digit codes returned by a server to indicate the result of a client's HTTP request.

They help the client, such as:

* Browser
* Frontend application
* Mobile application
* Another API

understand whether the request was successful or whether something went wrong.

### Main Categories

| Status Code | Category     | Meaning                                   |
| ----------- | ------------ | ----------------------------------------- |
| `2xx`       | Success      | Request was successfully processed        |
| `3xx`       | Redirection  | Further action or redirection is required |
| `4xx`       | Client Error | Problem with the client's request         |
| `5xx`       | Server Error | Problem occurred on the server            |

### Common Status Codes

```text
200 → OK
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

---

# HTTP Exception

**`HTTPException`** is a built-in FastAPI exception used to return a custom HTTP error response when something goes wrong.

Instead of returning a normal successful JSON response, we can gracefully raise an HTTP error.

### Example

```python
from fastapi import HTTPException

if patient is None:
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
```

The API will return:

```json
{
    "detail": "Patient not found"
}
```

This allows the API to clearly communicate what went wrong to the client.

---

# Query Parameters

**Query Parameters** are optional key-value pairs appended to the end of a URL to provide additional information to the server.

They are commonly used for:

* Filtering
* Sorting
* Searching
* Pagination

### Example

```http
GET /patients?city=Delhi
```

Here:

```text
city = Delhi
```

is a query parameter.

Multiple query parameters are separated using `&`.

```http
GET /patients?city=Delhi&age=30
```

Here we have:

```text
city = Delhi
age = 30
```

Query parameters allow us to perform additional operations **without changing the endpoint path itself**.

For example:

```text
/patients
```

can remain the same while query parameters control how the data should be retrieved.

---

# `Query()`

`Query()` is a FastAPI utility function used to declare, validate, and document query parameters in an API endpoint.

It allows us to define:

* Default values
* Validation rules
* Titles
* Descriptions
* Examples
* Length constraints

### Example

```python
from fastapi import Query

@app.get("/patients")
def get_patients(
    limit: int = Query(
        default=10,
        gt=0,
        le=100,
        description="Number of patients to return"
    )
):
    return {"limit": limit}
```

Now we can call:

```http
GET /patients?limit=20
```

FastAPI will automatically validate the value.

For example:

```http
GET /patients?limit=-5
```

will fail validation because:

```python
gt=0
```

requires the value to be greater than `0`.

---

# 11/09/2026

# Why Pydantic?

Consider a simple function for inserting patient data:

```python
def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:

        if age < 0:
            raise TypeError("Age should be positive")

        else:
            print(name)
            print(age)
            print("Inserted into database")

    else:
        raise TypeError("Incorrect data type")
```

If we pass:

```python
insert_patient_data("Nitish", "30")
```

the value `"30"` is a string instead of an integer.

We could manually validate this, but this approach does not scale well.

As an application grows, we may need to validate many different things:

* Data types
* Required fields
* Optional fields
* String lengths
* Numeric ranges
* Email formats
* Custom validation rules
* Nested objects

Writing manual validation logic for each function would make the code repetitive and difficult to maintain.

This is one of the problems Pydantic helps solve.

---

# Pydantic Validation

Pydantic allows us to define the expected structure of our data using a model.

The model defines:

* Expected fields
* Expected data types
* Validation constraints

### Example

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

Now Pydantic knows that:

```text
name → string
age  → integer
```

If the input does not match the expected structure or validation rules, Pydantic raises a validation error.

---

# How Pydantic Works

The process can be understood in three steps.

## Step 1 — Define the Pydantic Model

Define the expected fields, their types, and validation constraints.

```python
class Patient(BaseModel):
    name: str
    age: int
```

---

## Step 2 — Create the Object with Raw Input

We provide the raw input to the Pydantic model.

```python
patient = Patient(
    name="Nitish",
    age=30
)
```

Pydantic validates the data while creating the model object.

If the data is invalid, a validation error is raised.

---

## Step 3 — Pass the Validated Model to the Function

Once the data has been validated, we can pass the model object to our application logic.

```python
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
```

The function now works with structured and validated data instead of repeatedly performing manual validation.

---

# Pydantic Validation Flow

```text
Raw Input
    ↓
Pydantic Model
    ↓
Validation
    ↓
Valid Data
    ↓
Application / Business Logic
    ↓
Database
```

If validation fails:

```text
Raw Input
    ↓
Pydantic Model
    ↓
Validation
    ↓
Invalid Data
    ↓
Validation Error
```

This helps keep **validation logic separate from application logic**.

---

# 14/09/2026

# POST Endpoint

A **POST endpoint** is commonly used to create a new resource.

For example, when creating a new patient, the client sends patient information to the server in **JSON format**.

This JSON data is sent inside the **request body**.

A request body is the portion of an HTTP request that contains data sent by the client to the server.

It is commonly used with HTTP methods such as:

* `POST`
* `PUT`
* `PATCH`

### Example

```http
POST /patients
```

Request body:

```json
{
    "name": "Nitish",
    "age": 30,
    "city": "Delhi"
}
```

---

# POST Endpoint Flow

The overall flow can be understood as:

```text
Client
   ↓
POST Request
   ↓
Request Body
   ↓
FastAPI
   ↓
Pydantic Model
   ↓
Validation
   ↓
Validated Data
   ↓
Application Logic
   ↓
Database
   ↓
Response
```

The important idea is that the data should be validated before it is used by the application or inserted into the database.

---

# Update Endpoint

An **Update Endpoint** is used to modify an existing resource.

The resource is generally identified using a **Path Parameter**.

For example:

```http
PUT /patients/101
```

Here:

```text
101
```

is the patient ID that identifies the resource we want to update.

The fields that need to be updated are sent in the **request body**.

### Example

```json
{
    "name": "Nitish Kumar",
    "age": 31,
    "city": "Delhi"
}
```

---

# Why Do We Need a Separate Pydantic Model for Update?

Suppose our POST model is:

```python
class Patient(BaseModel):
    name: str
    age: int
    city: str
```

Here, all fields are required.

This makes sense when creating a new patient because we need the required patient information.

However, when updating a patient, we may want to change only one field.

For example:

```json
{
    "age": 31
}
```

If we use the same model, `name` and `city` would also be required.

Therefore, we create a separate Pydantic model for updating the patient where the fields can be optional.

### Example

```python
class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    city: str | None = None
```

Now the client can provide only the fields that need to be changed.

For example:

```json
{
    "age": 31
}
```

---

# Update Endpoint Flow

```text
Client
   ↓
PUT /patients/{id}
   ↓
Path Parameter
   ↓
Identify Patient
   ↓
Request Body
   ↓
Pydantic Update Model
   ↓
Validation
   ↓
Update Database
   ↓
Response
```

The **Path Parameter** identifies *which resource* should be updated, while the **Request Body** contains *what data should be updated*.

---

# Delete Endpoint

A **DELETE endpoint** is used to delete an existing resource.

The resource is generally identified using a path parameter.

### Example

```http
DELETE /patients/101
```

Here:

```text
101
```

identifies the patient that should be deleted.

---

# Delete Endpoint Flow

```text
Client
   ↓
DELETE /patients/{id}
   ↓
Path Parameter
   ↓
Find Patient
   ↓
Patient Found?
   ├── No  → HTTP 404 Exception
   │
   └── Yes
        ↓
     Delete Patient
        ↓
      Response
```

If the requested patient does not exist, the API can raise an `HTTPException` with a `404 Not Found` status code.

---

# CRUD Implementation Summary

The concepts learned can now be connected with the CRUD operations of the Patient Management API.

| Operation | HTTP Method | Input                         | Purpose                    |
| --------- | ----------- | ----------------------------- | -------------------------- |
| Create    | `POST`      | Request Body                  | Create a new patient       |
| Read      | `GET`       | Path / Query Parameters       | Retrieve patient data      |
| Update    | `PUT`       | Path Parameter + Request Body | Update an existing patient |
| Delete    | `DELETE`    | Path Parameter                | Delete an existing patient |

---

# Complete Request Flow

```text
                         CLIENT
                            │
                            │ HTTP Request
                            ↓
                         FastAPI
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ↓              ↓              ↓
        Path Params    Query Params    Request Body
             │              │              │
             │              │              ↓
             │              │         Pydantic
             │              │              │
             │              │              ↓
             │              │         Validation
             │              │              │
             └──────────────┼──────────────┘
                            ↓
                     Application Logic
                            │
                            ↓
                         Database
                            │
                            ↓
                         Response
                            │
                            ↓
                          Client
```

---

# Key Concepts Learned

| Concept         | Purpose                                         |
| --------------- | ----------------------------------------------- |
| Path Parameter  | Identifies a specific resource through the URL  |
| `Path()`        | Validates and documents path parameters         |
| Query Parameter | Provides additional information through the URL |
| `Query()`       | Validates and documents query parameters        |
| Request Body    | Carries structured data from client to server   |
| Pydantic        | Validates and parses structured data            |
| `HTTPException` | Returns meaningful HTTP errors                  |
| POST            | Creates a resource                              |
| PUT             | Updates/replaces a resource                     |
| DELETE          | Deletes a resource                              |
| CRUD            | Create, Read, Update, Delete                    |

---

# Overall Learning Flow

```text
API Fundamentals
      ↓
FastAPI
      ↓
HTTP Request / Response
      ↓
Path Parameters
      ↓
Query Parameters
      ↓
HTTP Status Codes
      ↓
HTTPException
      ↓
Pydantic
      ↓
Request Body
      ↓
POST
      ↓
PUT
      ↓
DELETE
      ↓
CRUD API
```
