**********SSH Multiple Servers Program

	Programming Language used : Python
	Platform : Linux
	Python version : Python 2.7
	Python Module Used : ParallelSSHClient

Description of code : 
	This program uses ParallelSSHClient module for running commands in multiple servers parallel. The code gets the hosts name in the command line arguments. And gets the input from the user which is the command for running in multiple servers. If the user enters the Numbers instead of commands then the program disconnects the connection and exit.

Executing the code:
	python ssh_multiple_servers.py h1 h2 h3 h4 h5
	Here h1,h2,h3,h4, h5 are the hosts names of the server for running the commands.

Output:
 	Here I dont know any hosts name. So I am giving dummy hosts name for execution. So the program rasies an exception saying UnknownHostException
	
[root@oc5275012015 Documents]# python ssh_multiple_servers.py h1 h2 h3 h4 h5
['ssh_multiple_servers.py', 'h1', 'h2', 'h3', 'h4', 'h5']
<type 'list'>
['h1', 'h2', 'h3', 'h4', 'h5']

Enter commands or type number to disconnect : ls
No handlers could be found for logger "pssh"
Traceback (most recent call last):
  File "/usr/lib64/python2.6/site-packages/gevent/greenlet.py", line 327, in run
    result = self._run(*self.args, **self.kwargs)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 522, in _exec_command
    proxy_port=self.proxy_port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 152, in __init__
    self._connect(self.client, self.host, self.port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 192, in _connect
    self.host, retries, self.num_retries)
UnknownHostException: ('%s - %s - retry %s/%s', 'Name or service not known', 'h4', 3, 3)
<Greenlet at 0x7f6687e0e190: <bound method ParallelSSHClient._exec_command of <pssh.ParallelSSHClient object at 0x7f6691a5e8d0>>('h4', 'ls', sudo=True)> failed with UnknownHostException

Traceback (most recent call last):
  File "/usr/lib64/python2.6/site-packages/gevent/greenlet.py", line 327, in run
    result = self._run(*self.args, **self.kwargs)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 522, in _exec_command
    proxy_port=self.proxy_port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 152, in __init__
    self._connect(self.client, self.host, self.port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 192, in _connect
    self.host, retries, self.num_retries)
UnknownHostException: ('%s - %s - retry %s/%s', 'Name or service not known', 'h3', 3, 3)
<Greenlet at 0x7f6687e0e0f0: <bound method ParallelSSHClient._exec_command of <pssh.ParallelSSHClient object at 0x7f6691a5e8d0>>('h3', 'ls', sudo=True)> failed with UnknownHostException

Traceback (most recent call last):
  File "/usr/lib64/python2.6/site-packages/gevent/greenlet.py", line 327, in run
    result = self._run(*self.args, **self.kwargs)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 522, in _exec_command
    proxy_port=self.proxy_port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 152, in __init__
    self._connect(self.client, self.host, self.port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 192, in _connect
    self.host, retries, self.num_retries)
UnknownHostException: ('%s - %s - retry %s/%s', 'Name or service not known', 'h5', 3, 3)
<Greenlet at 0x7f6687e0e230: <bound method ParallelSSHClient._exec_command of <pssh.ParallelSSHClient object at 0x7f6691a5e8d0>>('h5', 'ls', sudo=True)> failed with UnknownHostException

Traceback (most recent call last):
  File "/usr/lib64/python2.6/site-packages/gevent/greenlet.py", line 327, in run
    result = self._run(*self.args, **self.kwargs)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 522, in _exec_command
    proxy_port=self.proxy_port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 152, in __init__
    self._connect(self.client, self.host, self.port)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 189, in _connect
    retries=retries+1)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 192, in _connect
    self.host, retries, self.num_retries)
UnknownHostException: ('%s - %s - retry %s/%s', 'Name or service not known', 'h1', 3, 3)
<Greenlet at 0x7f6688aa5f50: <bound method ParallelSSHClient._exec_command of <pssh.ParallelSSHClient object at 0x7f6691a5e8d0>>('h1', 'ls', sudo=True)> failed with UnknownHostException

Traceback (most recent call last):
  File "ssh_multiple_servers.py", line 17, in <module>
    output = client.run_command(command, sudo=True)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 494, in run_command
    return self.get_output(commands=cmds)
  File "/usr/lib/python2.6/site-packages/pssh.py", line 561, in get_output
    (channel, host, stdout, stderr) = cmd.get()
  File "/usr/lib64/python2.6/site-packages/gevent/greenlet.py", line 274, in get
    raise self._exception
pssh.UnknownHostException: ('%s - %s - retry %s/%s', 'Name or service not known', 'h1', 3, 3)


