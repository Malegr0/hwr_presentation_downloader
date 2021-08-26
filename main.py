#!/usr/bin/python
# -*- coding:utf-8 -*-

from data import server

if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=5007)
