import requests, getpass, time

a = getpass.getpass('enter pass:')
passwords = ['abc',a]

url = ''
headers = {	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0',
    		'Referer': ''}
data = {'login':'','passwd':a}

with open('citrixLog.txt','a+') as f:
	for i in a:
		r = requests.post(url, headers=headers, data=data)
		f.write(r.text)
		if 'vpn' in r.text:
			pass
		else:
			print('[+] Match found: {}'.format(i))
			f.write('[+] Match found: {}'.format(i))
			f.write('='*50)
	print('Sleeping for 30 minutes')
	time.sleep(620)
	print('Sleeping for 20 minutes')
	time.sleep(620)
	print('Sleeping for 10 minutes')
	time.sleep(620)