# Backend Coding Rules (Python/FastAPI)

- **Framework**: Use FastAPI for all API endpoints.
- **Type Hinting**: All function signatures must include Python type hints for arguments and return types.
- **Data Validation**: Use Pydantic models (schemas) for all request and response bodies.
- **Async/Await**: Use asynchronous database drivers and `async def` for route handlers whenever possible.
- **Error Handling**: Use FastAPI's `HTTPException` for returning error responses to the client.
- **Code Style**: Follow PEP 8 guidelines. Use `black` for formatting if available.
- **Project Structure**:
    - `main.py`: Entry point for the FastAPI app.
    - `models/`: SQLAlchemy or other ORM models.
    - `schemas/`: Pydantic models for validation and serialization.
    - `api/`: Route definitions organized by feature.
