# COMMANDS

## Start up project

```bash

docker-compose build --no-cache && docker-compose up

```

## Run server

If you need to run the server and you have previously built the images:

```bash
docker-compose up
```

## Database connection

Open Docker postgres service and type on the exec console:

```bash
psql -h localhost -U postgres -d postgres -W
```

`password` is also postgres

## Django admin custom commands

It is advisable to run this commands on backend service, on the exec console

```bash
python manage.py load_data
```

This loads the data from .csv to the database. You must ensure you made migrations & migrated, before using this.

```bash
python manage.py populate_machine_runtimes
```

This populates the table `MachineRuntime` with the `.csv` data. It does calculations and after calculing the runtime of the machines,
it write the results of each date, to the table.

```bash
python manage.py calculate_machine_runtimes
```

This does the 24-hours runtime calculation. 