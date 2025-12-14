docker commands

# from the mycelery folder (where Docker-compose.yml is)
docker compose -f Docker-compose.yml up -d --build

# check logs
docker compose logs -f djangoproject
docker compose logs -f celery
docker compose logs -f celery-beat