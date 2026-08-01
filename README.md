# F1 Data Project

A Python-based Formula 1 data management application using the Jolpica F1 API.

The project is designed to collect, process, and store Formula 1 data while gradually expanding into a larger analytics platform.

---

## Current Features

### Data Import

Currently supported:

- Drivers
- Constructors
- Circuits

Data is retrieved from the Jolpica F1 API, processed into Python objects, and stored locally as JSON files.

---

## Project Structure

'''
F1_Project/

├── api/
│ └── jolpica.py
│
├── models/
│ ├── driver.py
│ ├── constructor.py
│ └── circuits.py
│
├── services/
│ ├── driver_service.py
│ ├── constructors_service.py
│ ├── circuits_services.py
│ └── data_service.py
│
├── data/
│ ├── 2026/
│ ├── 2027/
│ └── archive/
│
├── config.py
├── main.py
└── README.md
'''

---

## Technologies Used

- Python
- REST API
- JSON
- Git
- Jolpica F1 API

---

## Current Data Flow
Jolpica F1 API
    ↓
API Layer
    ↓
Service Layer
    ↓
Model Objects
    ↓
JSON Storage

---

## Running the Application

Activate the virtual environment:
venv\Scripts\activate

Run the application:
python main.py


---

## Current Menu Options

The application currently supports:
1. Import Drivers
2. List Drivers
3. Import Constructors
4. List Constructors
5. Import Circuits
6. List Circuits
0. Exit

---

## Future Development Goals

Planned future features include:

- Race calendar management
- Race results
- Driver standings
- Constructor standings
- Historical season archives
- F1 statistics and analytics
- Data visualisation
- Simulation features

---
