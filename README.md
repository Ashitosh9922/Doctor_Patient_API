# Doctor_Patient_API

A simple Django REST Framework API for managing doctors, patients, and appointments.

---


##Techstack:
Language: Python
Framework: Django + Django REST Framework
Database: SQLite

## API Endpoints

| Endpoint                    | Method | Description                        |
|-----------------------------|--------|----------------------------------|
| `/doctors/`                 | GET    | Get a list of all doctors        |
| `/doctors/<int:id>/`        | GET    | Get details of a specific doctor |
| `/doctors/create/`          | POST   | Register a new doctor            |
| `/appointments/`            | POST   | Book a new appointment           |
| `/appointments/list/`       | GET    | List all appointments            |

*Assuming the server runs at* `http://localhost:8000/`.


