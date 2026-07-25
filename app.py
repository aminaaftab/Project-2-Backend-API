"""
DecodeLabs - Project 2: Backend API Development
-------------------------------------------------



from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------------------------------------------------------
# "Database" (in-memory list, just for this training project)
# ---------------------------------------------------------
users = [
    {"id": 1, "name": "Aisha Khan", "email": "aisha@example.com"},
    {"id": 2, "name": "Rohan Mehta", "email": "rohan@example.com"},
]


def get_next_id():
    """Generate the next unique id for a new user."""
    if len(users) == 0:
        return 1
    return users[-1]["id"] + 1


# ---------------------------------------------------------
# ROUTE 1: GET /users -> Get the list of ALL users
# ---------------------------------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "success": True,
        "count": len(users),
        "data": users
    }), 200


# ---------------------------------------------------------
# ROUTE 2: GET /users/<id> -> Get ONE specific user by id
# ---------------------------------------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if user is None:
        # 404 = Not Found
        return jsonify({
            "success": False,
            "message": f"User with id {user_id} not found."
        }), 404

    return jsonify({"success": True, "data": user}), 200


# ---------------------------------------------------------
# ROUTE 3: POST /users -> Create a NEW user
# ---------------------------------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")

    # --- VALIDATION (Gatekeeper Rule: "Never trust the client") ---
    if not name or not isinstance(name, str) or name.strip() == "":
        return jsonify({
            "success": False,
            "message": "Validation failed: 'name' is required and must be text."
        }), 400

    if not email or not isinstance(email, str) or "@" not in email:
        return jsonify({
            "success": False,
            "message": "Validation failed: 'email' is required and must be valid."
        }), 400

    # Check for duplicate email
    if any(u["email"] == email for u in users):
        return jsonify({
            "success": False,
            "message": "A user with this email already exists."
        }), 400

    # --- If validation passes, create the user ---
    new_user = {
        "id": get_next_id(),
        "name": name.strip(),
        "email": email.strip()
    }
    users.append(new_user)

    # 201 = Created
    return jsonify({
        "success": True,
        "message": "User created successfully.",
        "data": new_user
    }), 201


# ---------------------------------------------------------
# ROUTE 4 (bonus): DELETE /users/<id> -> Remove a user
# ---------------------------------------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if user is None:
        return jsonify({
            "success": False,
            "message": f"User with id {user_id} not found."
        }), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({
        "success": True,
        "message": f"User with id {user_id} deleted."
    }), 200


# ---------------------------------------------------------
# 404 handler for undefined routes
# ---------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "message": "Route not found."}), 404


# ---------------------------------------------------------
# 500 handler for unexpected server errors
# ---------------------------------------------------------
@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "message": "Something went wrong on the server."}), 500


# ---------------------------------------------------------
# Start the server
# ---------------------------------------------------------
if __name__ == "__main__":
    print("✅ Server running at http://localhost:3000")
    print("Try: GET http://localhost:3000/users")
    app.run(port=3000, debug=True)
