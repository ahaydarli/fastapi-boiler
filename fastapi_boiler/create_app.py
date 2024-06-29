import os
import shutil
import click
import importlib.resources as resources


@click.command()
@click.option('--name', prompt='Project directory', help='The name of the project.')
@click.option('--version', prompt='Python version (3.10, 3.11, etc.)', help='Python version of the project.')
@click.option('--description', prompt='Description', help='The description of the project.')
@click.option('--author', prompt='Author', help='The author of the project.')
def create_app(name, version, description, author):
    """
    Create a new FastAPI app from a boilerplate template.

    Args:
        name (str): The name of the new application directory to create.
        version (str): The python version of the new application.
        description (str): The project description to use in pyproject.toml.
        author (str): The project author to use in pyproject.toml.
    """
    # Define the source directory for the boilerplate
    src_dir = resources.files('fastapi_boiler').joinpath('fastapi_boilerplate')

    # Define the destination directory for the new app
    dest_dir = os.path.join(os.getcwd(), name)

    try:
        # Check if the destination directory already exists
        if os.path.exists(dest_dir):
            print(f"Directory {name} already exists")
            return

        # Copy the boilerplate template to the destination directory
        shutil.copytree(src_dir, dest_dir)
        print(f"Copied template from {src_dir} to {dest_dir}")

        # Update the pyproject.toml file with the new project details
        pyproject_path = os.path.join(dest_dir, 'pyproject.toml')
        if os.path.exists(pyproject_path):
            with open(pyproject_path, 'r') as file:
                pyproject_content = file.read()

            # Replace placeholders with user-provided values
            pyproject_content = pyproject_content.replace('fastapi_boilerplate', name)
            pyproject_content = pyproject_content.replace('fastapi-boilerplate', name)
            pyproject_content = pyproject_content.replace('description = ""', f'description = "{description}"')
            pyproject_content = pyproject_content.replace('<example@example.com>', author)
            pyproject_content = pyproject_content.replace('3.11', version)

            with open(pyproject_path, 'w') as file:
                file.write(pyproject_content)
            print("Updated pyproject.toml with the new project details")

        # Update the docker-compose.yml file with the new app name
        docker_compose_path = os.path.join(dest_dir, 'docker-compose.yml')
        if os.path.exists(docker_compose_path):
            with open(docker_compose_path, 'r') as file:
                docker_compose_content = file.read()

            docker_compose_content = docker_compose_content.replace('boilerplate-api', name)

            with open(docker_compose_path, 'w') as file:
                file.write(docker_compose_content)
            print("Updated docker-compose.yml with the new app name")

        print(f"New FastAPI app created at {dest_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_app()
