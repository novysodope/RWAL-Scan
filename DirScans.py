# -*- coding: utf-8 -*-
 
from multiprocessing import Pool
from tqdm import tqdm
import requests
import re
import sys
import argparse
requests.packages.urllib3.disable_warnings()  #关闭ssl控制台报错
 
header = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
urllist = []
 

def mainshow():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', default='url.txt',help="URL文件路径")
    parser.add_argument('-f','--file', default='dict.txt',help="字典文件路径")
    parser.add_argument('-t','--threads', default='20',help="进程数，不要超过60")
    args = parser.parse_args()
 
    urllist = open_url(args.url)
    po = Pool(int(args.threads))
      #进度条显示
    pbar = tqdm(total=len(urllist))
    pbar.set_description('任务进度')
    update = lambda *args: pbar.update()
    #进度条显示
    for url in urllist:
        po.apply_async(run,(url,), callback=update)
    po.close()
    po.join()

def save(data,length,Server,title):
    f = open(r'批量扫描结果-200.txt', 'a+',encoding='utf-8')
    f.write(data + '\n')
    f.close()
    f2 = open(r'批量扫描详情-200.html', 'a+',encoding='utf-8')
    f2.write('<title>200-富婆批量扫描器</title><table><tr><td><a href="' + data + '" ' + 'target="_blank">' + data + '</a>&nbsp;</font>&nbsp;&nbsp;<br>服务器环境：[<font color="#FF0000">' + Server + '</font>]</a>&nbsp;&nbsp;<a>网站标题：[<font color="#FF0000">' + title + '</font>]&nbsp;&nbsp;Length：[<font color="FF0000">' + length + '</font>]</a></td></tr></table> <p></p><p></p>')
    f2.close()
def savetwo(data,length,Server,title):
    f = open(r'批量扫描结果-403.txt', 'a+',encoding='utf-8')
    f.write(data + '\n')
    f.close()
    f2 = open(r'批量扫描详情-403.html', 'a+',encoding='utf-8')
    f2.write('<title>403-富婆批量扫描器</title><table><tr><td><a href="' + data + '" ' + 'target="_blank">' + data + '</a>&nbsp;</font>&nbsp;&nbsp;<br>服务器环境：[<font color="#FF0000">' + Server + '</font>]</a>&nbsp;&nbsp;<a>网站标题：[<font color="#FF0000">' + title + '</font>]&nbsp;&nbsp;Length：[<font color="FF0000">' + length + '</font>]</a></td></tr></table> <p></p><p></p>')
    f2.close()
def savethree(data,length,Server,title):
    f = open(r'批量扫描结果-500.txt', 'a+',encoding='utf-8')
    f.write(data + '\n')
    f.close()
    f2 = open(r'批量扫描详情-500.html', 'a+',encoding='utf-8')
    f2.write('<title>500-富婆批量扫描器</title><table><tr><td><a href="' + data + '" ' + 'target="_blank">' + data + '</a>&nbsp;</font>&nbsp;&nbsp;<br>服务器环境：[<font color="#FF0000">' + Server + '</font>]</a>&nbsp;&nbsp;<a>网站标题：[<font color="#FF0000">' + title + '</font>]&nbsp;&nbsp;Length：[<font color="FF0000">' + length + '</font>]</a></td></tr></table> <p></p><p></p>')
    f2.close()
def savefour(data,length,Server,title):
    f = open(r'批量扫描结果-405.txt', 'a+',encoding='utf-8')
    f.write(data + '\n')
    f.close()
    f2 = open(r'批量扫描详情-405.html', 'a+',encoding='utf-8')
    f2.write('<title>405-富婆批量扫描器</title><table><tr><td><a href="' + data + '" ' + 'target="_blank">' + data + '</a>&nbsp;</font>&nbsp;&nbsp;<br>服务器环境：[<font color="#FF0000">' + Server + '</font>]</a>&nbsp;&nbsp;<a>网站标题：[<font color="#FF0000">' + title + '</font>]&nbsp;&nbsp;Length：[<font color="FF0000">' + length + '</font>]</a></td></tr></table> <p></p><p></p>')
    f2.close()

def open_url(url):
    f = open('dict.txt', 'r')
    # for i in f.readlines():
    dicttxt = f.readlines()
     # urls = i.rstrip('\n')
    with open(url) as f:
        for url in f:
            url = url.replace("\n","").split()
            for x in url:
                for i in dicttxt:
                    url = x + i.replace("\n","")
                    urllist.append(url)
    return(urllist)

def run(url):
    try:
        html = requests.get(url, headers=header,verify=False,timeout=(2,2))
        html.encoding = 'utf-8'
        code = html.status_code
        length = html.headers['Content-Length']
        title=re.findall('<title>(.+)</title>',html.content.decode("utf-8"))
        Server = html.headers['Server']
        # if Server:
        #   pass
        # else:
        #   Server = 'null'
        # # result = "application" in html 
        # # result2 = "application/json" in html
        # title=re.findall('<title>(.+)</title>',html)
        # if title:
        #   pass
        # else:
        #   title=re.findall('\"error\"\:\"(.+)\",\"message\"',html)
        #   if title:
        #     pass
        #   else:
        #     title = ['标题获取异常']
        if code == 200:
            print('\033[0;32m'+'\n'+'[+] 目标：%s  %s --length %s\032[0m'%(url,code,length)+'\n\033[0m')
            if title:
                title = title[0]
            else:
                title = "标题获取异常"
            save(url,length,Server,title)
        if code == 403:
            print('\033[1;33m'+'\n'+'[!] 目标：%s  %s --length %s\033[0m'%(url,code,length)+'\n\033[0m')
            if title:
                title = title[0]
            else:
                title = "标题获取异常"
            savetwo(url,length,Server,title)
        if code == 500:
            print('\033[0;31m'+'\n'+'[*] 目标：%s  %s --length %s\033[0m'%(url,code,length)+'\n\033[0m')
            if title:
                title = title[0]
            else:
                title = "标题获取异常"
            savethree(url,length,Server,title)
        if code == 405:
            print('\033[0;33m'+'\n'+'[*] 目标：%s  %s --length %s\033[0m'%(url,code,length)+'\n\033[0m')
            if title:
                title = title[0]
            else:
                title = "标题获取异常"
            savefour(url,length,Server,title)
            # result = open(r'Done_urls-200.html', 'a+')
            # result.write('<title>批量扫描_200-富婆扫描器</title>200页面：<table><tr><td><a href="' + url + '" ' + 'target="_blank">' + url + '</a>&nbsp;</font><br><a>网站标题：[<font color="#FF0000">' + title[0] + '</font>]&nbsp;&nbsp;服务器环境：[<font color="#FF0000">' + Server + '</font>]</a>&nbsp;&nbsp;<br><a>Length：[<font color="FF0000">' + length + '</font>]</a></td></tr></table>')
            # result.write('\r\n</br>')
            # result.close()
    except Exception as e:
      pass
    # except Exception as e:
    #   print()
 
if __name__ == '__main__':
    print('\n\n--------------------fengx NB!!!!-----------------\n\n')
    mainshow()