#!/usr/bin/python
# -*- coding:utf-8 -*-
import imgkit
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pdfkit



def get_pdf_from_url(website_url: str) -> str:
    """
    Method to receive the html text of an url.

    :param website_url: String of the url which will be searched for
    :return: complete html text as string
    """
    path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path)
    pdfkit.from_url(website_url, r'.\exports\out.pdf', configuration=config)
