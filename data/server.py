#!/usr/bin/python
# -*- coding:utf-8 -*-

import flask
from flask import request, render_template
from data import crawler

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hwr_pdf_downloader():
    link = request.args.get('link')
    if link is None or len(link) < 1:
        return render_template('pdf_downloader.html')
    crawler.get_pdf_from_url(link)
    return "Done"
