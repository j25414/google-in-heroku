import os
from wsgiref.simple_server import make_server

def application(environ,start_response):
    response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    status='200 OK'
    response_headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

port=int(os.environ.get("PORT",5000))
httpd=make_server('0.0.0.0',port,application)
httpd.serve_forever()


