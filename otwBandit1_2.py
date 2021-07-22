"""#############################################################################
##  PROGRAM:    OverTheWire BANDIT 1 -> BANDIT 2
##  FILENAME:   otwBandit1_2.py
##  AUTHOR:     0m3g4b1u3
#############################################################################"""
##  IMPORT(S)  ##
import paramiko

##  VARIABLE(S)  ##
host = 'bandit.labs.overthewire.org'
port = 2220
username = 'bandit1'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'

##  START SSH CLIENT  ##
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

##  COMMAND(S)  ##
cmd = 'ls -la\n'
cmd += 'cat ./-'

##  RUN COMMAND(S)  ##
stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)
