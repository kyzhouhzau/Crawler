#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Author:zhoukaiyin
给一个gene列表获取genecards中的相关信息。
"""
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.genecards.org',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'rvcn=dYIWz5EY6caGwWb3tjAvVBi99yAGdRP3eMJdEpXVqw7ujIwDYaD_cvpqUXiBzjEnqcMz_mOicUT7SgVGk3r8XwbS4Do1; raygun4js-userid=2ccb939f-1731-4a98-bbae-d1dd7168c971; __gads=ID=fabafac07decace7:T=1542266579:S=ALNI_MYzQMMlweVgBC3kbolw8ijByuqDtw; visid_incap_229828=kBXMmquRQbiX5Gwmg/EGDBxn9VsAAAAAQUIPAAAAAAAjYrAiSZ6H9W01u8RFKXGW; OUTFOX_SEARCH_USER_ID_NCOO=1404623155.5559037; ASP.NET_SessionId=nlqi114qlwmqmszeijj1qdml; ARRAffinity=71ac8b0d911f40963b4f9d1a64565710ea9816ad0321f794af3cfbc4c41b07db; nlbi_146342=dj58Lq+aEH7iii5Gi3zamgAAAACWnIDfRmIpxfS8UxSACdU3; incap_ses_893_146342=2hSON/NGYQ3z9A59UJNkDHh+9lsAAAAA2xgEFi8UAzSqrwFVnn6g5g==; _gat=1; visid_incap_146342=6uycfwzRQ+KtvmvdllZYc8ge7VsAAAAAREIPAAAAAACAvF+IAdrHRPvqR1Mu1pi+JJZRj/lZoRWt; incap_ses_434_146342=NXNifK8VcwcAUlWmX+EFBii/91sAAAAApCYGHE+aqFHDo5l2SAFnfA==; _ga=GA1.2.1734920045.1542245279; _gid=GA1.2.1498137442.1542770207; __atuvc=2%7C46%2C68%7C47; __atuvs=5bf7bf2d46bddc20000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
}

def get_page(url):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code==200:
            return response.content.decode('utf-8')
        return None
    except RequestException:
        return None

def pase_page(html,genename):
    if html!=None:
        soup = BeautifulSoup(html,'xml')
        pathway = soup.find_all(attrs={'data-type':'SuperPathway'})
        pathwaydir = {}
        if len(pathway)!=0 and len(pathway[0].select('tbody'))!=0:
            table = pathway[0].select('tbody')[0]
            for ul in table.select('tr td'):
                all_pathway = ul.find_all('a')
                for a in all_pathway:
                    pathwaydir[a.text] = a.attrs["href"]
        else:
            with open('./data/gene_data/faild.txt','a') as wf:
                wf.write(genename+'\n')
                pathwaydir = {}

        drugs = soup.find_all(attrs={'id':'drugs_compounds'})
        drugsdir = {}
        if len(drugs)!=0 and len(drugs[0].select('tbody'))!=0:
            table = drugs[0].select('tbody')[0]
            for tr in table.select('tr'):
                contents = []
                for td in tr.select('td'):
                    if td.a!=None:
                        content = td.a.attrs["href"]
                    else:
                        content = td.text
                    contents.append(content)
                druginfo = "{}####{}####{}####{}####" \
                           "{}####{}####{}".\
                            format(contents[0],contents[1],
                                    contents[2],contents[3],
                                    contents[4],contents[5],
                                    contents[6])
                drugsdir[contents[0]] = druginfo
        else:
            with open('./data/gene_data/faild.txt','a') as wf:
                wf.write(genename+'\n')
                drugsdir = {}
        return pathwaydir,drugsdir
    else:
        pathwaydir = {}
        drugsdir = {}
        return pathwaydir,drugsdir
def test():
    genename =  "RNF213&keywords=RNF213#pathways_interactions"
    url = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="
    url = url +genename
    html = get_page(url)
    pathwaydir, drugsdir = pase_page(html, genename)
    gene_pathway = "{}\t{}".format(genename, pathwaydir)
    gene_drug = "{}\t{}".format(genename, drugsdir)
    print(gene_drug)

def main():
    with open('./data/gene_data/allgene.txt') as rf:
        with open('./data/gene_data/gene_pathway.txt','a') as gp:
            with open('./data/gene_data/gene_drug.txt','a') as gd:
                with open('./data/gene_data/success_gene.txt','a') as forsuccess:
                    for line in rf:
                        genename = line.strip()
                        url = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="
                        url = url+genename+"&keywords="+genename+"#pathways_interactions"
                        html = get_page(url)
                        pathwaydir,drugsdir = pase_page(html,genename)
                        gene_pathway = "{}\t{}".format(genename,pathwaydir)
                        gene_drug = "{}\t{}".format(genename,drugsdir)
                        print(gene_drug)
                        gp.write(gene_pathway+'\n')
                        gd.write(gene_drug+'\n')
                        forsuccess.write(genename+'\n')
                        print("完成了对基因{}的爬取。".format(genename))
                        time.sleep(5)


if __name__=="__main__":
    # test()
    main()