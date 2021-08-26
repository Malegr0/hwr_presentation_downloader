#!/usr/bin/python
# -*- coding:utf-8 -*-

import flask
import json
from PyPDF2 import PdfFileMerger
from flask import request, render_template
from data import crawler

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hwr_pdf_downloader():
    link = request.args.get('link')
    if link is None or len(link) < 1:
        return render_template('pdf_downloader.html')
    json_paths = json.load(open(r'.\resources\config.json'))
    urls = crawler.get_all_addresses_from_url(link)
    i = 1
    for url in urls:
        output_path = json_paths['resource_path'] + str(i) + ".pdf"
        crawler.get_pdf_from_url(url, output_path, json_paths['wkhtmltopdf'])
        i += 1

    return "Done"
