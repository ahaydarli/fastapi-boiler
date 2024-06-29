# FastAPI Boilerplate

This is a boilerplate project for building a web application using FastAPI, Peewee ORM, and MySQL. The project is configured to use Poetry for dependency management and includes setup for handling exceptions, middleware, and application settings.

## Features

- FastAPI for building fast and efficient web APIs.
- Peewee ORM for database interactions.
- MySQL as the database.
- Structured project layout.
- Exception handling and middleware setup.
- Configuration management using Pydantic.

## Getting Started

### Prerequisites

- Python 3.11+
- Poetry

### Installation

1. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

### Running the Application

1. Start the FastAPI application using Uvicorn:
    ```bash
    poetry run uvicorn server:app --reload
    ```

2. Access the API documentation:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running Tests

1. Run tests using pytest:
    ```bash
    poetry run pytest
    ```

## Configuration

Application settings are managed using Pydantic. Configuration can be customized by editing the `settings/config.py` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or support, please contact [example@example.com](mailto:example@example.com).

