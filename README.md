# RsBaM Vertretungsplan Project

Welcome to the RsBaM Vertretungsplan Project! This project was specifically designed for the Realschule Bad Münstereifel to provide an API endpoint to upload, safe and show the "Vertretungsplan" in an (web-)app.

## What is a Vertretungsplan?

A "Vertretungsplan" is a German term that refers to a substitution plan or schedule. Schools use it to notify teachers and students about changes in their regular schedule due to absent teachers or other unforeseen events. It helps ensure that the educational process is not disrupted, and everyone is informed about who will be taking over a particular class or if there are any room changes.

## Features

1. **PostgreSQL Database Connection**: All the data regarding the Vertretungsplan is stored in a PostgreSQL database, ensuring smooth data transactions and management using SQLAlchemy.
2. **Vertretungsplan Endpoints**: Simple endpoints that teachers can access to retrieve the latest Vertretungsplan updates and changes.
3. **Authorization Checks**: To make sure only the school's staff can access the data, we have set up simple authorization checks that rely on authentication tokens.

## API Endpoints

`Content-Type: application/json`

### Requests
| Name | Method | Description | Body |
|----------|----------|----------|----------|
| `/api/{version}/vertretungsplan` | GET | Retrieve Vertretungsplan Data | -
| `/api/{version}/administration/hochladen` | POST | Upload JSON Vertretungsplan Data (for admin use) | JSON data



## Feedback & Support

If you're a teacher or a staff member at the school and have questions or feedback, please reach out to `contact at miguelcz dot com`.
