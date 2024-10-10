# Nylas Demo API

Welcome to the **Nylas Demo API**. This project demonstrates a basic setup for a Python Flask application that connects to the Nylas API. Please follow the instructions below to set up the environment and run the application.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- **Python 3.6+**: You can check if Python 3 is installed by running:
  
  ```bash
  python3 --version
  
- If Python 3 is not installed, you can download and install it from the official Python website.

- **Virtualenv**: Check if virtualenv is installed:

  ```bash
  virtualenv --version

- If not installed, you can install it via pip:
  ```bash
  pip install virtualenv
  ```

## Setup
- Clone the repo using below command:
  
  ```bash
  git clone git@github.com:SubashPradhan/nylas-demo-api.git
  ```

- Navigate to the project:
  
  ```bash
  cd nylas-demo-api
  ```

- **Create Virtual Environment**

  ```bash
  python3 -m venv venv
  ```

- Activate Virtual environment

  For Linux/macOS, run:
    ```bash
    source venv/bin/activate
    ```
  For Windows, run:
    ```bash
    venv\Scripts\activate
    ```
- **Install project dependencies**:

  ```bash
  pip install -r requirements.txt
  ```

## Run the application
  ```bash
  python run.py

```

The API endpoints can be accessed via port 8000 at the following URL: http://127.0.0.1:8000

For example: http://127.0.0.1:8000/health
  
### Happy Coding! 🚀
