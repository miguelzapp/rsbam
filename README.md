# RS BaM Vertretungsplan Project

This project was specifically designed for the Realschule Bad Münstereifel to provide a basic REST API server to upload, save and show the "Vertretungsplan" in an (web-)app.

## What is a Vertretungsplan?

A "Vertretungsplan" is a German term that refers to a substitution plan or schedule. Schools use it to notify teachers and students about changes in their regular schedule due to absent teachers or other unforeseen events. It helps ensure that the educational process is not disrupted, and everyone is informed about who will be taking over a particular class or if there are any room changes.

## Features

1. **PostgreSQL Database Connection**: All the data regarding the Vertretungsplan is stored in a PostgreSQL database, ensuring smooth data transactions and management using SQLAlchemy.
2. **Vertretungsplan Endpoints**: Simple endpoints that teachers can access to retrieve the latest Vertretungsplan updates and changes.
3. **Authorization Checks**: To make sure only the school's staff can access the data, we have set up simple authorization checks that rely on authentication tokens.

## API Endpoints

```
Content-Type: application/json
Authorization: Bearer <token>
```

| Name                                      | Method | Description                                      | Req. Body | Res. Body
|-------------------------------------------|--------|--------------------------------------------------|-----------|----------
| `/api/{version}/vertretungsplan`          | GET    | Retrieve Vertretungsplan Data                    | -         | DateTime, latest JSON data
| `/api/{version}/administration/hochladen` | POST   | Upload JSON Vertretungsplan Data (for admin use) | JSON data | -

## Running the Server

Before running the server, configure `db_auth.py` and `auth.py`.

To run the REST API server, the provided `rsbam.service` systemd service file is used. This service ensures the server starts after the PostgreSQL service.

#### Service Configuration:
- **Description**: RsBaM Vertretungsplan API-Server
- **ExecStart Command**: This uses `uwsgi` to run the server, bound to `127.0.0.1:6000`.
- **Working Directory**: `/home/user/rsbam` 
- **User**: `user`

  
#### Start the server:

1. Move the `rsbam.service` file to `/etc/systemd/system/`.
2. Reload the systemd manager configuration:  
  
   ```
   sudo systemctl daemon-reload
   ```
3. Start the service:  
   ```
   sudo systemctl start rsbam.service
   ```
4. (Optional) To enable the service to start on boot:  
   ```
   sudo systemctl enable rsbam.service
   ```
   
## Feedback & Support

If you're a teacher or a staff member at the school and have questions or feedback, please reach out to `contact at miguelcz dot com`.
