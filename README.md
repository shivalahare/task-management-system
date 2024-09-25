
# Task Management System

This is a Django-based Task management system.

## Installation

### Prerequisites

- Python 3.x
- Git
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/shivalahare/task-management-system.git
```

Navigate to the project directory:

```bash
cd task_management
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

#### For Ubuntu/Linux:

1. Install `python3-venv` if not installed:

   ```bash
   sudo apt install python3-venv
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

#### For Windows:

1. Install `virtualenv` if not installed:

   ```bash
   python -m pip install --user virtualenv
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```

### 3. Install Dependencies

Once the virtual environment is activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

1. Create migrations:

   ```bash
   python manage.py makemigrations
   ```

2. Apply the migrations:

   ```bash
   python manage.py migrate
   ```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

## Usage

You can now access the application at `http://127.0.0.1:8000/`.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
