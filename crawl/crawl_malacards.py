#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
"""
"""
给定一个疾病获取该疾病的所有 Pathway 和 drug信息

"""
import requests
import time
import pickle
import os
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
headers1 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.malacards.org',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1597716003.963064; ARRAffinity=4eabb5c0d966931ee925a8962ca2bcaf79daec3ec6c37f54ec5d2f84e5a720c1; nlbi_161858=oTukJJLlSia6nyJJ4tPBxgAAAACtS5LUvNr+N/QdH254NUPk; visid_incap_161858=KmDjT7ypS7uit5AlJiN0wEvK7FsAAAAAQUIPAAAAAACeQS8JB0B10VbnBSaXYs5k; incap_ses_463_161858=sMq1cfua3U1T+NMGPelsBr2J91sAAAAAe1ubxlCKwiEEhNFR1xWveA==; _ga=GA1.2.1063194696.1542244941; _gid=GA1.2.123935556.1542796513',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
}
headers2 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.malacards.org',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1597716003.963064; ARRAffinity=3c9bae3cfeca704eec61d00ee670371a6e725d0ce40a9af4532d1d41a65e42db; nlbi_161858=cWhYGbNGwyZWw3OM4tPBxgAAAAAxEe8qEJcam2ROCFo5Ks7c; incap_ses_463_161858=8MI0HPLXjQy52VcHPelsBoO6+FsAAAAAxYQ6X8z/4NwCJX5olm45NA==; incap_ses_541_161858=nag0elFy2WBXHa862gWCB0O8+FsAAAAA0Fwl8pQBWVcOKTxMLm2FZA==; ASP.NET_SessionId=hmiwvk4h4brb2dsrlhkakgrm; visid_incap_161858=KmDjT7ypS7uit5AlJiN0wEvK7FsAAAAAQUIPAAAAAACeQS8JB0B10VbnBSaXYs5k; incap_ses_199_161858=TFosVKSmyh4DW2fWhP7CAhu++FsAAAAAUNjAxnkvcrhRuYPFSCiDRA==; _ga=GA1.2.1063194696.1542244941; _gid=GA1.2.123935556.1542796513',
    # 'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1597716003.963064; ARRAffinity=3c9bae3cfeca704eec61d00ee670371a6e725d0ce40a9af4532d1d41a65e42db; nlbi_161858=cWhYGbNGwyZWw3OM4tPBxgAAAAAxEe8qEJcam2ROCFo5Ks7c; _gat=1; visid_incap_161858=KmDjT7ypS7uit5AlJiN0wEvK7FsAAAAAQUIPAAAAAACeQS8JB0B10VbnBSaXYs5k; incap_ses_463_161858=8MI0HPLXjQy52VcHPelsBoO6+FsAAAAAxYQ6X8z/4NwCJX5olm45NA==; _ga=GA1.2.1063194696.1542244941; _gid=GA1.2.123935556.1542796513',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
}
headers3 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.malacards.org',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1597716003.963064; ARRAffinity=3c9bae3cfeca704eec61d00ee670371a6e725d0ce40a9af4532d1d41a65e42db; nlbi_161858=cWhYGbNGwyZWw3OM4tPBxgAAAAAxEe8qEJcam2ROCFo5Ks7c; incap_ses_463_161858=8MI0HPLXjQy52VcHPelsBoO6+FsAAAAAxYQ6X8z/4NwCJX5olm45NA==; incap_ses_541_161858=nag0elFy2WBXHa862gWCB0O8+FsAAAAA0Fwl8pQBWVcOKTxMLm2FZA==; ASP.NET_SessionId=hmiwvk4h4brb2dsrlhkakgrm; visid_incap_161858=KmDjT7ypS7uit5AlJiN0wEvK7FsAAAAAQUIPAAAAAACeQS8JB0B10VbnBSaXYs5k; incap_ses_199_161858=TFosVKSmyh4DW2fWhP7CAhu++FsAAAAAUNjAxnkvcrhRuYPFSCiDRA==; _gat=1; _ga=GA1.2.1063194696.1542244941; _gid=GA1.2.123935556.1542796513',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
}
def get_page(url,headers):
    """
    根据某个网页获取该网页的html页面
    :param url:
    :param headers:
    :return:
    """
    try:
        response = requests.get(url,headers = headers)
        if response.status_code==200:
            return response.content.decode('utf-8')
        return None
    except RequestException:
        return None

def pase_page(html,genename):
    """
    解析网页获取pathway和drug信息。
    :param html:
    :param genename:
    :return:
    """
    if html!=None:
        soup = BeautifulSoup(html,'xml')
        pathway = soup.find_all(attrs={'id':'Pathway-table'})
        pathwaydir = {}
        if len(pathway)!=0 and len(pathway[0].select('tbody'))!=0:
            table = pathway[0].select('tbody')[0]
            for td in table.select('tr td'):
                all_pathway = td.find_all('div')
                for div in all_pathway:
                    if div.a!=None:
                        pathwaydir[div.a.text] = div.a.attrs["href"]
        else:
            with open('./data/disease_data/faild.txt','a') as wf:
                wf.write(genename+'\n')
                pathwaydir = {}

        drugs = soup.find_all(attrs={'id':'MaladiesUnifiedCompounds-table'})
        drugsdir = {}
        if len(drugs)!=0 and len(drugs[0].select('tbody'))!=0:
            table = drugs[0].select('tbody')[0]
            for tr in table.select('tr'):
                contents = []
                if len(tr.attrs)>0:
                    pass
                else:
                    for td in tr.select('td'):
                        if td.a!=None:
                            content = td.a.attrs["href"]
                        else:
                            content = td.text
                        contents.append(content)
                    if len(contents)==8:
                        druginfo = "{}####{}####{}####{}####" \
                                   "{}####{}####{}####{}".\
                                    format(contents[0].strip(),contents[1].strip(),
                                            contents[2].strip(),contents[3].strip(),
                                            contents[4].strip(),contents[5].strip(),
                                            contents[6].strip(),contents[7].strip())
                        drugsdir[contents[2]] = druginfo
                    else:
                        pass
        else:
            with open('./data/disease_data/faild.txt','a') as wf:
                wf.write(genename+'\n')
                drugsdir = {}
        return pathwaydir,drugsdir
    else:
        pathwaydir = {}
        drugsdir = {}
        return pathwaydir,drugsdir

def get_diseases(href,directionary):
    new_url = "https://www.malacards.org" + href
    html1 = get_page(new_url, headers3)
    soup1 = BeautifulSoup(html1, 'lxml')
    pheno = soup1.find_all(attrs={'class': 'search-results'})
    if len(pheno) != 0:
        trs = pheno[0].select('tr')
        for tr in trs:
            for td in tr.select('td'):
                if td.a != None:
                    href = td.a.attrs["href"]
                    name = td.a.text
                    directionary[name] =href

def get_url():
    """
    获取所有的疾病以及该疾病的连接。
    :return:
    """
    url = "https://www.malacards.org/categories"
    html = get_page(url,headers2)
    soup = BeautifulSoup(html,'xml')
    pheno = soup.find_all(attrs={'class':'search-results'})
    directionary = {}
    if len(pheno)!=0:
        trs = pheno[0].select('tr')
        for tr in trs:
            for td in tr.select('td'):
                if td.a!=None:
                    href = td.a.attrs["href"]
                    get_diseases(href, directionary)
    print(directionary)
    with open("./data/disease_data/directionary.pkl",'wb') as wf:
        pickle.dump(directionary,wf)
    return directionary

def normalize(name):
    name = name.lower().replace('-','').replace(' ','').replace(',','')
    return name

def main():

    if not os.path.exists("./data/disease_data/directionary.pkl"):
        get_url()
    else:
        with open("./data/disease_data/directionary.pkl", 'rb') as rf:
            dictionary = pickle.load(rf)
        disease_url = {}
        for name,url in dictionary.items():
            nname = normalize(name)
            disease_url[nname]=url
        rf =  open('./data/disease_data/allphenotype.txt')
        gp =  open('./data/disease_data/gene_pathway.txt','a')
        gd =  open('./data/disease_data/gene_drug.txt','a')
        forsuccess = open('./data/disease_data/success_gene.txt','a')
        for line in rf:
            phenoname = line.strip()
            phenoname = phenoname.replace('@', '')
            print(phenoname)
            # phenoname = "aicardi-goutieres syndrome 3"
            # url = get_url(phenoname)
            norname = normalize(phenoname)
            if norname in disease_url.keys():
                print("#############")
                url ="https://www.malacards.org" + disease_url[normalize(phenoname)]
                print(url)
                html = get_page(url,headers1)
                pathwaydir,drugsdir = pase_page(html,phenoname)
                pheno_pathway = "{}\t{}".format(phenoname, pathwaydir)
                pheno_drug = "{}\t{}".format(phenoname, drugsdir)
                gp.write(pheno_pathway + '\n')
                gd.write(pheno_drug + '\n')
                forsuccess.write(phenoname + '\n')
                print("完成了对基因{}的爬取。".format(phenoname))
                time.sleep(4)
        rf.close()
        gp.close()
        gd.close()
        forsuccess.close()

if __name__=="__main__":
    main()