# FastAPI Boiler

`fastapi-boiler` is a command-line tool for quickly generating a boilerplate FastAPI application. It streamlines the setup process, allowing you to get started with your FastAPI project quickly and efficiently.

## Features

- FastAPI boilerplate generation
- Dynamic project naming
- Customizable project metadata (author, description)
- Automatic Docker and Poetry configuration updates

## Installation

Install `fastapi-boiler` using pip.

```shell
pip install fastapi-boiler
```

## Usage

To create a new FastAPI application, run:

```shell
fastapi-boiler
```

You will be prompted to enter your app directory, description and email, which will be used to update the boilerplate configuration files.

### Example

```sh
$ fastapi-boiler
Project directory: testing
Python version (3.10, 3.11, etc.): 3.11
Description: test
Author: john.doe@mail.com
Copied template from fastapi_boilerplate to testing
Updated pyproject.toml with the new project details
Updated docker-compose.yml with the new app name
New FastAPI app created at testing
```

## Configuration

To make `fastapi-boiler` available globally, you may need to add the installation path to your shell configuration file.

### Bash

Add the following line to your `~/.bashrc` file:
```sh
export PATH="$HOME/.local/bin:$PATH"
```
Then, reload the `~/.bashrc` file:
```sh
source ~/.bashrc
```

### Zsh

Add the following line to your `~/.zshrc` file:

```sh
export PATH="$HOME/.local/bin:$PATH"
```
Then, reload the `~/.zshrc` file:
```sh
source ~/.zshrc
```


## Project Structure

After running the `fastapi-boiler` command, your new FastAPI application will have the following structure:

```shell
my_new_app/
├── app/
│   └── v1/
│       ├── health/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   └── views.py
│       ├── __init__.py
│       └── views.py
├── core/
│   ├── __init__.py
│   ├── database.py
│   ├── exception_handlers.py
│   ├── exceptions.py
│   ├── extensions.py
│   ├── factory.py
│   └── middlewares.py
├── settings/
│   └── config.py
├── tests/
│   └── __init__.py
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
├── requirements.txt
└── server.py
```

### Files and Directories

- **app/**: Contains the main application code.
  - **v1/**: API version 1.
    - **health/**: Health check endpoints.
    - **__init__.py**: Package initializer.
    - **router.py**: Router configuration.
    - **views.py**: Endpoint views.
- **core/**: Core functionality and utilities.
  - **database.py**: Database configuration.
  - **exception_handlers.py**: Custom exception handlers.
  - **exceptions.py**: Custom exception definitions.
  - **extensions.py**: Extensions and third-party integrations.
  - **factory.py**: Application factory.
  - **middlewares.py**: Custom middlewares.
- **settings/**: Configuration settings.
  - **config.py**: Main configuration file.
- **tests/**: Unit and integration tests.
- **docker-compose.yml**: Docker Compose configuration.
- **Dockerfile**: Dockerfile for containerizing the application.
- **pyproject.toml**: Poetry configuration file.
- **README.md**: Project readme file.
- **requirements.txt**: Project dependencies.
- **server.py**: Entry point for running the application.
- **create_app.py**: Script for creating a new FastAPI project.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or support, please contact [ali.heyderli@gmail.com](mailto:ali.heyderli@gmail.com).
