# Post_API
# Django Project with Docker

This is a Django project template that uses Docker for development and deployment.

## Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Project Structure

```
project/
├── app/
│   ├── manage.py
│   ├── your_django_app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── ...
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

- `app/`: Directory containing your Django project.
- `requirements.txt`: File listing Python dependencies.
- `Dockerfile`: Configuration for building the Docker image.
- `docker-compose.yml`: Configuration for running Docker containers.

## Getting Started

1. Clone this repository:

   ```bash
   git clone github.com/konstantine25b/Post_API
   cd Post_API
   ```

2. Build and start Docker containers:

   ```bash
   docker-compose up --build
   ```

3. Access your Django application at [http://localhost:8000](http://localhost:8000).
