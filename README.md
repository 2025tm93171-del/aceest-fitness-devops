# ACEest Fitness & Gym — DevOps CI/CD

## Project Overview

ACEest Fitness & Gym is a Python-based fitness management application. This repository preserves the original application versions and adds automated testing and CI/CD configuration.

The original application versions use Tkinter for the desktop interface. The CI pipeline runs automated tests without launching the graphical interface.

## Repository Contents

- `Aceestver-*.py` and related files: original application versions.
- `fitness_utils.py`: independently testable fitness utility functions.
- `tests/`: automated Pytest tests.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: container image used to run automated tests.
- `Jenkinsfile`: Jenkins pipeline definition.
- `.github/workflows/main.yml`: GitHub Actions workflow.

## Prerequisites

- Python 3.12
- pip
- Docker (for container builds)
- Jenkins (for Jenkins pipeline execution)

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest -v
```

## Run with Docker

Build the image:

```bash
docker build -t aceest-fitness:ci .
```

Run the container:

```bash
docker run --rm aceest-fitness:ci
```

The container runs the automated test suite. It does not launch the original Tkinter desktop application.

## CI/CD

### GitHub Actions

The workflow in `.github/workflows/main.yml` runs on pushes and pull requests. It installs dependencies, executes Pytest, and builds the Docker image.

### Jenkins

The `Jenkinsfile` defines checkout, dependency installation, testing, and Docker image build stages. Jenkins requires Python and Docker to be available to its build agent.

## Testing

The initial automated tests cover BMI calculation and membership-status utilities, including invalid inputs and membership expiry boundaries.

## Original Versions

All ten supplied Python versions are retained to preserve the development history of the application.