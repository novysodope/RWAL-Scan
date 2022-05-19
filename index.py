#!/usr/bin/etc python 2.7
#-*-coding:utf-8-*-
#!X3SCAN

import os,sys
import webbrowser
from DirScan import main
from UrlScan import main1

running = True
menu = """                                                                                   
   _____
   \\/,---<
   ( )@ @(      _         开门，查水表
    C __>/    |/ )
     \\\\//     |_/ 
   ,- >o<-.__/ /
  /   \\/  ____/ 
 / /|  | |
/ \'--/_| |
`----\\_) |
    |____|
    |  | |
    |  | |
    |  | |
    |__|_|_
    (____)_)    

       菜单  
--------------------
[+] 1: url状态探测
[+] 2: 目录扫描
[+] h: 帮助
[!] q: 退出
--------------------
"""

menu_dict={
      "h": "[!]请输入相应的数字",
	  #自适应咋写-.-
      "1": "df -h",
      "2": "free -m"
      }

def commands(args):
    cmd = menu_dict.get(args)
    return cmd
 
if __name__ == "__main__":
    os.system('cls')
    print (menu)   
    while running:
        cmd = input("[?]请输入你的命令:")
        if cmd != 'q':
            os.system('cls')
            try:
                print (menu)
                #列表开始，这里可以加进自己想插入的插件
				#可以这么写↓
				#if cmd == '序号':
                #os.system("文件名")
                if commands(cmd) != None:
                    if cmd == '1':
                        # os.system("UrlScan.py")
                        main1()

                    elif  cmd == '2':
                        #os.system("DirScan.py")
                        main()
                       
                    elif  cmd == 'h':
                        os.system("readme.txt")#自己看帮助，不要问我不要问我不要问我

                    else:
                        print (commands(cmd))
                else:
                    print ("[!]请重新输入!")
            except Exception as e:
                print (menu)
                print (e)
        else:
            print ('退出')
            os.system('cls')
            sys.exit()