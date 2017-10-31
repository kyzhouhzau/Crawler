#! usr/bin/env python3
# -*- coding:utf-8 -*-

from drugbank import Search_drugbank

def main():
    with open(r'C:\Users\zhouk\Desktop\100-drug.txt', 'r') as rf:
        line = rf.readlines()
    for word in line:
        sd = Search_drugbank(word.strip())
        print(sd.search())
        with open(r'zhoukaiyin.txt','a') as wf:
            wf.write(str(sd.search())+'\n')
            wf.close()

if __name__ == '__main__':
    main()