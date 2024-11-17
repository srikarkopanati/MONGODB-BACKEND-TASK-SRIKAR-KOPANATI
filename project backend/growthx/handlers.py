import tornado.ioloop
import tornado.web
import json
from models import users, assignments, admins
from bson.objectid import ObjectId

class RegisterUserHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        if "userId" not in data or "password" not in data:
            self.set_status(400)
            self.write({"error": "Missing required fields."})
            return
        users.insert_one({
            "userId": data["userId"],
            "password": data["password"] 
        })
        self.write({"message": "User registered successfully."})

class LoginUserHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        user = users.find_one({"userId": data["userId"], "password": data["password"]})
        if user:
            self.write({"message": "Login successful."})
        else:
            self.set_status(401)
            self.write({"error": "Invalid credentials."})

class UploadAssignmentHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        if "userId" not in data or "task" not in data or "admin" not in data:
            self.set_status(400)
            self.write({"error": "Missing required fields."})
            return
        assignments.insert_one({
            "userId": data["userId"],
            "task": data["task"],
            "admin": data["admin"],
            "status": "pending",
            "createdAt": data.get("createdAt", "pending")
        })
        self.write({"message": "Assignment uploaded successfully."})

class ViewAssignmentsHandler(tornado.web.RequestHandler):
    def get(self):
        admin = self.get_argument("admin", None)
        if not admin:
            self.set_status(400)
            self.write({"error": "Missing admin parameter."})
            return
        tasks = list(assignments.find({"admin": admin, "status": "pending"}))
        self.write({"tasks": tasks})

class AcceptAssignmentHandler(tornado.web.RequestHandler):
    def post(self, assignment_id):
        task = assignments.find_one({"_id": ObjectId(assignment_id)})
        if not task:
            self.set_status(404)
            self.write({"error": "Assignment not found."})
            return
        assignments.update_one({"_id": ObjectId(assignment_id)}, {"$set": {"status": "accepted"}})
        self.write({"message": "Assignment accepted."})

class RejectAssignmentHandler(tornado.web.RequestHandler):
    def post(self, assignment_id):
        task = assignments.find_one({"_id": ObjectId(assignment_id)})
        if not task:
            self.set_status(404)
            self.write({"error": "Assignment not found."})
            return
        assignments.update_one({"_id": ObjectId(assignment_id)}, {"$set": {"status": "rejected"}})
        self.write({"message": "Assignment rejected."})
