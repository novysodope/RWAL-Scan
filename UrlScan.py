#!coding:utf-8
import sys
import threading
import requests
import signal
import random
from queue import Queue
from optparse import OptionParser
from colorama import Fore,Back,Style
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import urllib.request
import re
import time


def agent_list():
  agents = [
    {'User-Agent': 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.9.1.15) Gecko/20101027 Fedora/3.5.15-1.fc12 Firefox/3.5.15'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko/2008092809 Gentoo Firefox/3.0.2'},
    {'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0'},
    {'User-Agent': 'Opera/9.10 (Windows NT 5.2; U; en)'},
    {'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko)'},
    {'User-Agent': 'Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51'}]

  return random.choice(agents)


def main1():
 author = '''

.########..##......##.########...######...######.....###....##....##
.##.....##.##..##..##.##.....##.##....##.##....##...##.##...###...##
.##.....##.##..##..##.##.....##.##.......##........##...##..####..##
.########..##..##..##.##.....##..######..##.......##.....##.##.##.##
.##...##...##..##..##.##.....##.......##.##.......#########.##..####
.##....##..##..##..##.##.....##.##....##.##....##.##.....##.##...###
.##.....##..###..###..########...######...######..##.....##.##....##
                                          
 Rich Woman URL Scanner --富婆URL状态探测器 v1.0
 by: novy\n\n'''
 print(Fore.BLUE + author)
 parser = OptionParser('python run.py -u <目标文件> [-t <线程数，不输入默认10>]，\n\n示例：\npython3 run.py -u url.txt')
 parser.add_option('-u', dest='url', type='string', help='要扫描的目标')
 parser.add_option('-t', dest='count', type='int', default=10, help='线程数')
 (options, args) = parser.parse_args()
 if options.url:
   PathScan = RWALScan(options)
   PathScan.start()
   sys.exit(1)
 else:
   parser.print_help()
   sys.exit(1)
# try:
#   while 1:
#     pass
# except KeyboardInterrupt:
#   quit()
class RWALScan:
  def __init__(self, options):
    self.url = options.url
    self.count = options.count

  class PathScan(threading.Thread):
    """
    多线程
    """
    def __init__(self, queue, total):
      threading.Thread.__init__(self)
      self._queue = queue
      self._total = total

    def run(self):
      while not self._queue.empty():
        url = self._queue.get()
        # 多线程显示进度
        threading.Thread(target=self.msg).start()
        xxx = agent_list()
        try:
        	r = requests.get(url=url,headers=xxx,timeout=5)
        	code=r.status_code
        	if code:
        		html = r.content.decode("utf-8")
        		title=re.findall('<title>(.+)</title>',html)
        		if title:
        			pass
        		else:
        			title=re.findall('\"error\"\:\"(.+)\",\"message\"',html)
        			if title:
        				pass
        			else:
        				title = ['标题获取异常']
        		print('\r\n%s '% code+'[+]%s' % url+'   '+title[0])
        except Exception:
        	pass

    def msg(self):
      per = 100 - float(self._queue.qsize()) / float(self._total) * 100
      percent = "已扫描 %s 个| 总共 %s 个| 已完成 %1.f %s" % (
        (self._total - self._queue.qsize()), self._total, per,"%")
      sys.stdout.write('\r' + '[*]' + percent)

  def start(self):
    queue = Queue()
    f = open(sys.argv[2] ,'r')
    for i in f.readlines():
      queue.put(i.rstrip('\n'))
    total = queue.qsize()
    threads = []
    thread_count = int(self.count)
    for i in range(thread_count):
      threads.append(self.PathScan(queue, total))
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()
 

if __name__ == '__main__':

   main1()
