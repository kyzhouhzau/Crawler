#! usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import requests
from  selenium import webdriver
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.PhantomJS()
wait = WebDriverWait(browser,10)
browser.set_window_size(1400,900)


class Search_drugbank(object):

    def __init__(self,keys):
        self.keys = keys

    def search(self):
        base_url = 'https://www.drugbank.ca/drugs'
        try:
            browser.get(base_url)
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#query"))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"#main-nav > form > button"))
            )
            input.send_keys(self.keys)
            submit.click()
            html = browser.page_source
            url = re.search('<div.*?result-info.*?hit-name.*?href="(.*?)".*?</div>', html, re.S)
            return self.print_result(url.group(1))
        except TimeoutError:
            return self.search()

    def print_result(self,url):
        base_url = 'https://www.drugbank.ca/drugs'
        patten = re.compile('tbody.*?<tr>.*?<td>.*?<strong>(.*?)'
                            '</strong>.*?<td>.*?<strong>(.*?)</td>'
                            '.*?<tr>.*?<tr>.*?<td>(.*?)</td>',re.S)
        response = requests.get(urljoin(base_url,url))
        html = response.text
        results = re.search(patten,html)
        return {
            'Word':self.keys,
            'Name':results.group(1),
            'Accession Number':results.group(2).replace('</strong>&nbsp;','').replace(',','').replace('</strong>',''),
            'Groups':results.group(3).replace(',',' ')
            }




