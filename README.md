# Fund Finder Backend

This repository contains the backend application for the Fund Finder project, built using Django. It is containerized with Docker to ensure a consistent and reliable development environment. The project follows best practices for development, testing, and deployment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Branching Strategy](#branching-strategy)
- [Testing Procedures](#testing-procedures)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Fund Finder is a hybrid recommender system to help users find funding opportunities effectively. This repository hosts the backend, which includes API endpoints, database management, and business logic.

## Prerequisites

Before starting, ensure you have the following tools installed on your machine:

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python (optional)](https://www.python.org/) - For debugging or manual Django management commands.

## Setup Instructions

Follow these steps to set up the development environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd fund_finder_backend
   ```

2. **Create an Environment File**:
   Copy the example environment file and customize it as needed:
   ```bash
   cp envs/.env.example envs/.env.dev
   ```

3. **Update Environment Variables**:
   Open `envs/.env.dev` and fill in the required values, such as database credentials and secret keys.

4. **Build and Run Docker Containers**:
   ```bash
   docker-compose -f docker/compose.dev.yml up --build
   ```

5. **Access the Application**:
   - Backend: [http://localhost:8080](http://localhost:8080)
   - Admin Panel: [http://localhost:8080/admin](http://localhost:8080/admin)

6. **Run Migrations**:
   Initialize the database by applying migrations:
   ```bash
   docker exec -it fund_finder_backend python manage.py migrate
   ```

7. **Create a Superuser**:
   Create an admin account for accessing the Django admin panel:
   ```bash
   docker exec -it fund_finder_backend python manage.py createsuperuser
   ```

## Branching Strategy

The project follows a Git Flow branching model:

- **dev**: Active development happens here.
- **staging**: Pre-production testing.
- **prod**: Production-ready, live code.
- **Feature Branches**: Used for individual features or fixes. Example: `feature/add-api`.
- **Release Branches**: Used for preparing releases. Example: `release/v1.0`.
- **Hotfix Branches**: For critical fixes in production. Example: `hotfix/fix-bug`.

## Testing Procedures

Testing ensures application stability and reliability. The following tests are included:

- **Unit Tests**: Validate individual functions or modules.
- **Integration Tests**: Test interactions between components.
- **System Tests**: End-to-end testing of the application.
- **Performance Tests**: Test speed and scalability under load.
- **Security Tests**: Identify vulnerabilities like SQL injection or XSS.

Run tests using the following command:
```bash
docker exec -it fund_finder_backend python manage.py test
```

## Best Practices

1. **Write Tests Early**: Ensure sufficient test coverage for new features.
2. **Use Environment Variables**: Avoid hardcoding sensitive values; use `.env` files.
3. **Follow Code Standards**: Adhere to PEP 8 and project-specific guidelines.
4. **Code Reviews**: Submit pull requests for review before merging.
5. **Database Migrations**: Always run migrations when modifying models.

## Contributing

1. Fork the repository and create a feature branch.
2. Write your code and tests.
3. Submit a pull request to the `dev` branch for review.

## License

This project is licensed under the MIT License.

---

For further questions or support, contact the project team.
