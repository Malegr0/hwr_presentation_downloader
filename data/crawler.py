#!/usr/bin/python
# -*- coding:utf-8 -*-

import pdfkit
import requests


def get_pdf_from_url(website_url: str):
    """
    Method to receive the html text of an url.

    :param website_url: String of the url which will be searched for
    :return: complete html text as string
    """
    path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path)
    pdfkit.from_url(website_url, r'.\resources\exports\out.pdf', configuration=config)


def get_all_addresses_from_url(website_url: str) -> list:
    while website_url[-1] != '/':
        website_url = website_url[:-1]
    response_code = 404
    i = 1
    urls = []
    while True:
        try:
            request_url = website_url + str(i)
            r = requests.head(request_url)
            if r.status_code == response_code:
                break
            urls.append(request_url)
            i += 1
        except requests.ConnectionError:
            print("failed to connect")
    return urls
