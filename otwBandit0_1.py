"""#############################################################################
##  PROGRAM:    OverTheWire BANDIT 0 -> BANDIT 1 (paramiko)
##  FILENAME:   otwBandit0_1.py
##  AUTHOR:     0m3g4b1u3
#############################################################################"""
##  IMPORT(S)  ##
import paramiko

##  VARIABLE(S)  ##
host = 'bandit.labs.overthewire.org'
port = 2220
username = 'bandit0'
password = 'bandit0'

##  START SSH CLIENT  ##
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

##  COMMAND(S)  ##
cmd = 'ls -la\n'        #   ADD \n after each command
cmd += 'cat readme'     #   LAST command doesn't need \n

##  RUN COMMAND(S)  ##
stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)
