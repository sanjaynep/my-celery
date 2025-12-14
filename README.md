# My Celery

A Django project demonstrating **Celery** integration for asynchronous and scheduled task processing.  This project showcases how to set up automated email notifications using Celery Beat with Redis as the message broker.

## What Does This Project Do?

This project is a practical example of implementing **background task processing** and **scheduled tasks** in Django using Celery.  Specifically, it: 

- **Automated Email Scheduling**: Sends automated emails at regular intervals (every 10 seconds) using Celery Beat
- **Asynchronous Task Processing**: Offloads email sending to background workers, keeping the main Django application responsive
- **Redis Message Broker**: Uses Redis to queue and manage tasks between Django and Celery workers
- **Docker Containerization**: Provides a fully containerized setup with Django, Celery Worker, Celery Beat, and Redis services

### How It Works

1. **Celery Beat** (scheduler) triggers the `send_email_task` every 10 seconds
2. The task is pushed to **Redis** (message broker)
3. **Celery Worker** picks up the task from Redis
4. The worker executes the task - sending an email via SMTP (Gmail)

```
┌─────────────┐     ┌─────────┐     ┌────────────────┐     ┌──────────┐
│ Celery Beat │ --> │  Redis  │ --> │ Celery Worker  │ --> │  Gmail   │
│ (Scheduler) │     │ (Queue) │     │ (Task Runner)  │     │  (SMTP)  │
└─────────────┘     └─────────┘     └────────────────┘     └──────────┘
```

## Tech Stack

- **Python** 3.13+
- **Django** 6.0+
- **Celery** 5.6+ with Redis backend
- **Redis** - Message broker
- **Docker** & Docker Compose for containerization
- **uv** - Python package manager

## Project Structure

```
my-celery/
├── core/                   # Django app with Celery tasks
│   ├── tasks.py           # Celery task definitions (email sending)
│   ├── models.py
│   ├── views.py
│   └── ... 
├── mycelery/              # Django project configuration
│   ├── celery.py          # Celery app configuration
│   ├── settings.py        # Django settings (Celery Beat schedule, email config)
│   ├── Dockerfile
│   └── Docker-compose. yml
├── manage.py
├── pyproject.toml
└── uv.lock
```

## Prerequisites

- Python 3.13 or higher
- Docker and Docker Compose
- Gmail account with App Password (for email functionality)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/sanjaynep/my-celery.git
   cd my-celery
   ```

2. Create a `.env` file in the `mycelery` folder with the following variables:
   ```env
   celery_url=redis://redis:6379/0
   EMAIL_NAME=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   ```

3. Navigate to the mycelery folder and start the services:
   ```bash
   cd mycelery
   docker compose -f Docker-compose.yml up -d --build
   ```


### Local Development

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/sanjaynep/my-celery.git
   cd my-celery
   uv sync
   ```

2. Set up environment variables (create a `.env` file):
   ```env
   celery_url=redis://localhost:6379/0
   EMAIL_NAME=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   ```

3. Start Redis (using Docker):
   ```bash
   docker run -d -p 6379:6379 redis:latest
   ```

4. Run migrations and start Django:
   ```bash
   uv run manage.py migrate
   uv run manage.py runserver
   ```

5. In a separate terminal, start the Celery worker:
   ```bash
   uv run celery -A mycelery worker --loglevel=info
   ```

6. In another terminal, start Celery Beat:
   ```bash
   uv run celery -A mycelery beat --loglevel=info
   ```

## Docker Commands

### Start all services
```bash
cd mycelery
docker compose -f Docker-compose.yml up -d --build
```

### View logs
```bash
# Django project logs
docker compose logs -f djangoproject

# Celery worker logs
docker compose logs -f celery

# Celery Beat logs
docker compose logs -f celery-beat
```

### Stop all services
```bash
docker compose -f Docker-compose.yml down
```

## Configuration

### Celery Beat Schedule

The scheduled task is configured in `mycelery/settings.py`:

```python
CELERY_BEAT_SCHEDULE = {
    'send-email-every-10-seconds':  {
        'task': 'core.tasks.send_email_task',
        'schedule': 10.0,  # every 10 seconds
    },
}
```

### Email Configuration

Email is sent using Gmail SMTP. Make sure to:
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password for this application
3. Add the credentials to your `.env` file

## Dependencies

| Package | Version |
|---------|---------|
| Django | >=6.0 |
| Celery (with Redis) | >=5.6.0 |
| python-decouple | >=3.8 |

## Use Cases

This project serves as a template for:
- 📧 Automated email notifications
- ⏰ Scheduled background jobs
- 📊 Report generation at intervals
- 🔄 Periodic data synchronization
- 📱 Push notification systems

## License

This project is open source and available under the [MIT License](LICENSE).docker commands

