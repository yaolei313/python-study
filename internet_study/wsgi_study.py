#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from wsgiref.simple_server import make_server, demo_app

httpd = make_server('', 8080, demo_app)
print('start server on port 8080...')
httpd.serve_forever()