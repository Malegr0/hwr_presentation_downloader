#!/usr/bin/python
# -*- coding:utf-8 -*-

import flask
import json
import os
from PyPDF2 import PdfFileMerger
from flask import request, render_template, send_from_directory
from data import crawler

app = flask.Flask(__name__, static_folder='..\\resources\\exports')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hwr_pdf_downloader():
    link = request.args.get('link')
    if link is None or len(link) < 1:
        return render_template('pdf_downloader.html')
    json_paths = json.load(open(r'.\resources\config.json'))
    urls = crawler.get_all_addresses_from_url(link)
    i = 1
    output_pdfs = []
    for url in urls:
        output_path = json_paths['resource_path'] + str(i) + ".pdf"
        crawler.get_pdf_from_url(url, output_path, json_paths['wkhtmltopdf'])
        output_pdfs.append(output_path)
        i += 1
    merger = PdfFileMerger()
    for pdf in output_pdfs:
        merger.append(pdf)
    merger.write(json_paths['resource_path'] + "result.pdf")
    merger.close()
    for pdf in output_pdfs:
        os.remove(pdf)
    return send_from_directory(app.static_folder, "result.pdf")
