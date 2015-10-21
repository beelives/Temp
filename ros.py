# -*- coding: utf-8 -*-
#!/usr/bin/
#加载模块
import paramiko
import sys
print '''sdfsfdsdfsdfsdfsfd
sdfsfsdf
sfsfd '''
#从命令行获取值
hostname=sys.argv[1]
port=22
username=sys.argv[2]
password=sys.argv[3]
#print sys.argv[1]
if __name__== '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname,username=username,password=password)
    #上传文件
    sftp = paramiko.SFTPClient.from_transport(s)
    #第一个文件
    remotepath='/tmp/66c221be-6ab2-ef53-1589-fe16877914f4.sh'
    localpath='F:/test/66c221be-6ab2-ef53-1589-fe16877914f4.sh'
    sftp.put(localpath,remotepath)
    #第二个文件
    remotepath1='/tmp/66c221be-6ab2-ef53-1589-fe16877914f4.pl'
    localpath1='F:/test/66c221be-6ab2-ef53-1589-fe16877914f4.pl'
    sftp.put(localpath1,remotepath1)
    #执行自定义命令
    stdin,stdout,stderr = s.exec_comma('ls -la /tmp/')
    print stdout.read()
    s.close()