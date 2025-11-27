# Task Flow API

## Project Structure

The `task_flow_api` project is organized into a three-layer architecture consisting of the following directories:
```
task_flow_api/
├── api.py          # API layer with routes for handling HTTP requests
├── service.py      # Business logic layer interacting with repository
├── repository.py   # Database interactions and CRUD operations
├── model.py        # Data models used in the application
├── db.py           # Database connection and schema initialization
├── pyproject.toml  # Project dependencies and configuration
└── README.md       # Project documentation and setup instructions
```

## Dev guide

To set up the project, follow these steps:
```bash
uv sync
```


To launch the FastAPI application, use the following command:

```bash
uv run uvicorn task_flow_api.main:app --reload
```

This command starts the server with auto-reload enabled, allowing you to see changes without restarting the server.

```bash
# Expected response: {"version":"1.0.0"}
curl 127.0.0.1:8000/version
```
 

## API Endpoints

The API provides endpoints for managing tasks. You can interact with the following endpoints:

- **GET /tasks**: Retrieve a list of tasks.
- **POST /tasks**: Create a new task.
- **GET /tasks/{id}**: Retrieve a specific task by ID.
- **PUT /tasks/{id}**: Update a specific task by ID.
- **DELETE /tasks/{id}**: Delete a specific task by ID.