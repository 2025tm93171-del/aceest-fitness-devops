# ACEest Fitness & Gym — DevOps CI/CD

## 1. Project Overview

ACEest Fitness & Gym is a Python-based fitness management application. This repository preserves the original application versions and adds automated testing and Continuous Integration/Continuous Delivery (CI/CD) configuration.

The original application versions use Tkinter for the desktop interface. To support automated testing in a headless environment, independently testable fitness utility functions and Pytest tests have been added. The CI pipelines execute these tests without launching the graphical interface.

## 2. Repository Contents

- `Aceestver-*.py` and related files: original application versions.
- `fitness_utils.py`: independently testable fitness utility functions.
- `tests/`: automated Pytest test suite.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: container image configuration for running automated tests.
- `Jenkinsfile`: Jenkins pipeline definition.
- `.github/workflows/main.yml`: GitHub Actions workflow.

## 3. Prerequisites

- Python 3.12
- pip
- Docker for container image builds
- Jenkins for Jenkins pipeline execution

## 4. Run Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the automated tests:

```bash
python -m pytest -v
```

## 5. Run with Docker

Build the Docker image:

```bash
docker build -t aceest-fitness:ci .
```

Run the container:

```bash
docker run --rm aceest-fitness:ci
```

The container executes the automated test suite. It does not launch the original Tkinter desktop application.

## 6. CI/CD Pipeline

### GitHub Actions

The workflow defined in `.github/workflows/main.yml` runs on pushes and pull requests. It checks out the repository, configures Python, installs dependencies, executes Pytest, and builds the Docker image.

### Jenkins

The `Jenkinsfile` defines the pipeline stages for source-code checkout, dependency installation, automated testing, and Docker image building. The Jenkins build agent requires Python, pip, and Docker to be available.

## 7. Automated Testing

The automated test suite uses Pytest to validate the fitness utility functions.

The tests cover:

- Valid BMI calculation.
- Invalid weight and height inputs.
- Active membership status.
- Expired membership status.
- Membership expiry-date boundary behavior.

**Test result:** All six automated tests passed in the verified Jenkins build.

## 8. Pipeline Verification

The CI/CD configuration was verified using both Jenkins and GitHub Actions.

- Jenkins pipeline: successful build.
- Automated testing: all six tests passed.
- Docker: image build completed successfully in Jenkins.
- GitHub Actions: workflow completed successfully, including the automated testing and Docker build steps.

Screenshots of the successful pipeline runs and test results are maintained as project evidence.

## 9. Original Application Versions

All ten supplied Python application versions are retained in the repository to preserve the original application files and development history.
