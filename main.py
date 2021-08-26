#!/usr/bin/python
# -*- coding:utf-8 -*-

from data import crawler
from data import server

if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=5007)
    #html_str = crawler.get_pdf_from_url("https://meet7.hwr-berlin.de/bigbluebutton/presentation"
    #                                    "/f7a5e4852ba06fd56f0e875ec62b3111eb631c17-1629902261234"
    #                                    "/f7a5e4852ba06fd56f0e875ec62b3111eb631c17-1629902261234"
    #                                   "/2640fb257cb584312c6fd78be225bdbc55afc931-1629903274033/svg/7")
