The Assignment Submission Portal is a web-based application designed to streamline the process of assignment submission and review. 
Users can register, log in, and upload assignments that are tagged to specific admins for review. Admins can log in, view the 
assignments assigned to them, and take actions by either accepting or rejecting them. This system provides a seamless way for users to 
submit their tasks and for admins to manage and evaluate the submissions. The backend of the application is built using Tornado, a high
-performance Python web framework, while MongoDB serves as the database for storing user credentials, assignments, and their statuses.

The portal relies on a simple HTML page as the frontend for user interaction. This page contains forms that allow users to register, 
log in, upload assignments, and for admins to view and manage assignments. JavaScript is used to send data between the frontend and the 
backend, making API calls to register users, log them in, upload tasks, and fetch pending assignments for admins. The application uses 
a RESTful API approach, where various HTTP methods are used to handle different functionalities like assignment submission and status 
updates. The system is designed to be intuitive and user-friendly, with clear forms for each task and appropriate feedback for each 
action.

In terms of database structure, the MongoDB database is organized into collections for users, admins, and assignments. Each user and 
admin is stored with relevant credentials, while assignments are stored with fields like userId, task, admin, and status. The assignment
data allows for easy tracking of the submission status, which can be updated by the admin. The combination of Tornado, MongoDB, and a 
basic HTML frontend ensures a smooth and responsive application suitable for managing assignments in educational or organizational 
settings.