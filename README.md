# Doctor_Patient_API

A simple Django REST Framework API for managing doctors, patients, and appointments.

---


## Tech Stack

- **Language:** Python  
- **Framework:** Django with Django REST Framework (DRF)  
- **Database:** SQLite


## API Endpoints

| Endpoint                    | Method | Description                        |
|-----------------------------|--------|----------------------------------|
| `/doctors/`                 | GET    | Get a list of all doctors        |
| `/doctors/<int:id>/`        | GET    | Get details of a specific doctor |
| `/doctors/create/`          | POST   | Register a new doctor            |
| `/appointments/`            | POST   | Book a new appointment           |
| `/appointments/list/`       | GET    | List all appointments            |

*Assuming the server runs at* `http://localhost:8000/`.


## Demo Images for APIs

**1. `GET /doctors/` – List all doctors**

<img width="1366" height="768" alt="Screenshot (225)" src="https://github.com/user-attachments/assets/6b9292e9-473f-4586-9428-eeb10078648e" />

**2. `GET /doctors/:id` – Get doctor details**

<img width="1366" height="768" alt="Screenshot (226)" src="https://github.com/user-attachments/assets/08de236e-543e-486e-9337-6c24be9b308b" />

**3. `POST /doctors/create/` – Create doctor**

<img width="1366" height="768" alt="Screenshot (228)" src="https://github.com/user-attachments/assets/7412e7bb-40ac-4b8a-8691-71bdf2e9ad59" />

**4. `POST /appointments/` – Book appointment**

<img width="1366" height="768" alt="Screenshot (229)" src="https://github.com/user-attachments/assets/652b7079-d988-4ef5-af29-9d332141f3a3" />

**5. `GET /appointments?doctor_id=` – Appointments for doctor**

<img width="1366" height="768" alt="Screenshot (230)" src="https://github.com/user-attachments/assets/152517ec-8f6b-4253-989d-894320766fff" />

**6. `GET /appointments?patient_id=` – Appointments for patient**

<img width="1366" height="768" alt="Screenshot (231)" src="https://github.com/user-attachments/assets/74e116f5-d9cb-421c-88d2-d8ecc09b9922" />


