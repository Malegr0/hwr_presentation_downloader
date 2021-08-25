#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests


def get_html_from_url(website_url: str) -> str:
    """
    Method to receive the html text of an url.

    :param website_url: String of the url which will be searched for
    :return: complete html text as string
    """
    html_website = requests.get(website_url)
    html_string = html_website.text
    return html_string
