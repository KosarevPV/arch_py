from wsgiref.simple_server import make_server

from framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)


with make_server('', 8000, application) as httpd:
    print("Запуск на порту 8080...http://127.0.0.1:8000/")
    httpd.serve_forever()

