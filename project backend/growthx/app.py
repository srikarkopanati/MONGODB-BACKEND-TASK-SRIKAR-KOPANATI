import tornado.ioloop
import tornado.web
from handlers import RegisterUserHandler, LoginUserHandler, UploadAssignmentHandler, ViewAssignmentsHandler, AcceptAssignmentHandler, RejectAssignmentHandler
from tornado.web import StaticFileHandler

def make_app():
    return tornado.web.Application([
        (r"/register", RegisterUserHandler),
        (r"/login", LoginUserHandler),
        (r"/upload", UploadAssignmentHandler),
        (r"/admins", ViewAssignmentsHandler),
        (r"/assignments/([^/]+)/accept", AcceptAssignmentHandler),
        (r"/assignments/([^/]+)/reject", RejectAssignmentHandler),
        (r"/(.*)", StaticFileHandler, {"path": "static", "default_filename": "index.html"}) 
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
