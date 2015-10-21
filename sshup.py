# -*- coding: utf-8 -*-  
#!/usr/bin/python
import paramiko
ssh = paramiko.Transport(("sys.argv[1]",22))
ssh.connect(username = "sys.argv[2]", password = "sys.argv[3]")
sftp = paramiko.SFTPClient.from_transport(ssh)
remotepath='/tmp/9b582aba-879c-a753-2b55-61cfbcea31c7.pl'
localpath='F:/test/9b582aba-879c-a753-2b55-61cfbcea31c7.pl'
sftp.put(localpath,remotepath)
remotepath1='/tmp/9b582aba-879c-a753-2b55-61cfbcea31c7.sh'
localpath1='F:/test/9b582aba-879c-a753-2b55-61cfbcea31c7.sh'
sftp.put(localpath1,remotepath1)
print "UP OK"
stdin,stdout,stderr = ssh.exec_command("ls")
print stdout.readlines()
ssh.close()