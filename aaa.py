#Create a directory named hacked inside /home/user/desktop where user is the username of any given comp
import os
import getpass
a=getpass.getuser()
'''os.chdir('/home')
os.chdir(a)
os.chdir('/Desktop')
os.mkdir('hacked')'''

b='cd /home/'
d='/Desktop'
e=b+a+d
os.system(e)
os.system('mkdir abc')

