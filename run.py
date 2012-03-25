import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


from app import app

if __name__ == '__main__':

	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(os.environ.get('PORT', 5000))
	IOLoop.instance().start()
