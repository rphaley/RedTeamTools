import requests, getpass, time

a = getpass.getpass('enter pass:')
passwords = ['abc',a]

url = ''
headers = {	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0',
    		'Referer': ''}
data = {'login':'','passwd':a}

for i in a:
	r = requests.post(url, headers=headers, data=data)
	print(r.text)

	if 'vpn' in r.text:
		print("no match")
	else:
		print('match found')
	print('Sleeping...')
	time.sleep(10)