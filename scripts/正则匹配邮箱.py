import re
str=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
if re.match(str,'hello.world@163.com'):
	print('OK')

if re.match(str,'hello.wo_rl-d1@163.com'):
	print('OK')