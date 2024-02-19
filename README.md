# maper-back-chall

## Backend Challenge jan-2024

## Goal

This challenge is from MAPER, and is intended to evaluate my ability to interpret requirements, think logically, design software with judgement, and write clean and modular code.

## Navigation
| Title                  | Link                                               |
|------------------------|----------------------------------------------------|
| API DOC                | [Go to API DOC](./app/api/README.md)               |
| CHALLENGE INSTRUCTIONS | [Go to CALLENGE INSTRUCTIONS](./CHALLENGE.md)      |
| SYSTEM EXPLANATION     | [Go to SYSTEM EXPLANATION](./ARCHITECTURE.md)      |
| COMMANDS               | [Go to COMMANDS](./COMMANDS.md)                    |

## Requirements:

- Docker Desktop

## Instructions

1. Startup project with 

```bash
docker-compose build --no-cache && docker-compose up
```

2. After initialization, check if migrations are made. If not, access the backend service and make them.

```bash
python manage.py makemigrations metrics sensors machine
```

```bash
python manage.py migrate
```

3. After making migrations, load the data from .csv to database, with this custom command:

```bash
python manage.py load_data
```
4. Load the database with the previous machine runtimes.

```bash
python manage.py populate_machine_runtimes
```

5. After putting services up, navigate to 

```
localhost:8000/swagger/
```

or

```
localhost:8000/redoc/
```

to see api docs.