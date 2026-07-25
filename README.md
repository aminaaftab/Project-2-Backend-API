# Project 2: Backend API Development (Python + Flask version)


## What this project does
- `GET /users` — get the list of all users
- `GET /users/<id>` — get one user by id
- `POST /users` — create a new user (with validation)
- `DELETE /users/<id>` — bonus: delete a user

## How to run it in VS Code

### Step 1: Check Python is installed
Open VS Code → Terminal → New Terminal, then type:
```
python3 --version
```
If you see a version number (e.g. `Python 3.12.3`), you're good.
If not, download Python from **python.org** (make sure to check
"Add Python to PATH" during install on Windows).

### Step 2: Open this folder in VS Code
File → Open Folder → select the folder with `app.py`, `requirements.txt`.

### Step 3: Install Flask
In the terminal:
```
pip install -r requirements.txt
```
(On Mac/Linux you might need `pip3` instead of `pip`.)

### Step 4: Run the server
```
python3 app.py
```
(On Windows it might just be `python app.py`.)

You should see:
```
✅ Server running at http://localhost:3000
```

### Step 5: Test it
Open your browser and go to:
```
http://localhost:3000/users
```
You'll see a JSON list of users.

## Testing POST (create a user)

Use **Postman** (postman.com, free) or curl:

```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Priya Sharma","email":"priya@example.com"}'
```

Try sending empty data too — you'll get a `400 Bad Request` with a
clear validation message, proving the API doesn't trust client input blindly.

## Screenshots

Below are screenshots showing the API working end-to-end.

### 1. Server running successfully
<img width="684" height="360" alt="terminal running" src="https://github.com/user-attachments/assets/22e9cb65-0ba7-4d36-92d6-b385451ceb5f" />


### 2. GET /users — fetching all users (browser)
<img width="400" height="328" alt="get endpoints" src="https://github.com/user-attachments/assets/79e6482c-f89c-47dc-aa27-c8b5af223d4a" />


### 3. POST /users — creating a new user (Postman, 201 Created)
<img width="664" height="504" alt="post endpoint" src="https://github.com/user-attachments/assets/7eb41f60-139e-4466-a908-48449c1a7943" />

### 3. POST /users — Data Validation (Postman, 400 Bad request)
<img width="661" height="423" alt="data validation" src="https://github.com/user-attachments/assets/08491a44-0483-44a9-86b1-28c35781882a" />


## How this maps to the project requirements

| Requirement                     | Where it's done in code                         |
|----------------------------------|--------------------------------------------------|
| Create API endpoints (GET/POST) | `@app.route("/users", methods=["GET"/"POST"])`   |
| Handle user input and responses | `request.get_json()`, `jsonify()`                |
| Validate basic data              | `if not name...`, `if not email...` checks       |
| Proper status codes              | 200, 201, 400, 404, 500 used correctly           |
| RESTful naming (nouns not verbs) | `/users` not `/getUsers` or `/createUser`        |
