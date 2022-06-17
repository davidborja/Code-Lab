# Code-Lab 

## Generate a new SSH key
### Generate-ssh: ssh-keygen -t ed25519 -C "your_email@example.com"
### Init agent-ssh: eval "$(ssh-agent -s)"
### Create config file: touch ~/.ssh/config
    ```
    Host *
      AddKeysToAgent yes
      UseKeychain yes
      IdentityFile ~/.ssh/id_ed25519
    ```

### Add public key: ssh-add -K ~/.ssh/id_ed25519
    
## Instalation Guide.

### 1.- First install virtualenv: pip3 install virtualenv

### 2.- create a environment: virtualenv -p python_path enviroment-lab

### 3.- Activate environment: source enviroment-lab/bin/activate

### 4.- Install requirements: pip install -r requirements.txt

## Precommit configuration

### 1.- install pre-commit: pre-commit install

## Creating Local Migrations

### create directory: python migrate.py db init --directory migrations_local
### create alembic code: python migrate.py db migrate --directory migrations_local
### sql code: python migrate.py db upgrade --directory migrations_local

## API Implementation

1. Using Flask or Django (preferably Flask), implement a RESTful API with a `GET` endpoint named `/api/v1/shopping/statistics` that returns the total of money spent grouped by category. This endpoint should also accept a request parameter named `category`. If such parameter is sent, we should only return that category total.

    NOTES:
    1. You don't need to implement any DB, you can use the test data below as the data source.
    2. Validations for error scenarios are not required.

    ### Test data:
    ```
    [
        {
            "code": "01827395",
            "name": "Bread",
            "category": "Food",
            "price": 5.30,
            "quantity": 2,
            "percentage_discount": 0
        },
        {
            "code": "17283640",
            "name": "Milk",
            "category": "Food",
            "price": 2.15,
            "quantity": 4,
            "percentage_discount": 10
        },
        {
            "code": "64902891",
            "name": "Computer mouse",
            "category": "Electronics",
            "price": 9.99,
            "quantity": 1,
            "percentage_discount": 15
        },
        {
            "code": "92730769",
            "name": "Soap",
            "category": "Personal hygiene",
            "price": 0.50,
            "quantity": 4,
            "percentage_discount": 7
        },
        {
            "code": "64729981",
            "name": "Pen",
            "category": "Office",
            "price": 0.25,
            "quantity": 10,
            "percentage_discount": 5
        },
        {
            "code": "86009275",
            "name": "Computer keyboard",
            "category": "Electronics",
            "price": 24.99,
            "quantity": 1,
            "percentage_discount": 12
        },
        {
            "code": "95741182",
            "name": "Toilet paper",
            "category": "Personal hygiene",
            "price": 3.15,
            "quantity": 2,
            "percentage_discount": 0.0
        },
        {
            "code": "95017233",
            "name": "Copier paper",
            "category": "Office",
            "price": 3.00,
            "quantity": 10,
            "percentage_discount": 30
        }
    ]
    ```

    ### Response format:
    ```
    GET /api/v1/shopping/statistics

    {
        "data": {
            "category-a": 0.00,
            "category-b": 0.00,
            ...
        }
    }
    ```

    ```
    GET /api/v1/shopping/statistics?category=category-c

    {
        "data": {
            "category-c": 0.00,
        }
    }
    ```

2. Create unit tests for the implemented endpoint.

3. Add any relevant information and instructions to run the application and tests in the `README.md` file inside the directory.

## Refactoring

1. Without using any lint, refactor `refactor_me.py`. Change ANYTHING that you think would be an improvement over the original code.

2. Add any reasoning or relevant information to the `README.md`.