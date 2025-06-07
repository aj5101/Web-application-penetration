import requests

target_url=input('[*] Enter target url: ')
file_name=input('[*] Enter file name containing directories: ')


def request(url):
	try:
		return requests.get("http://"+url)
	except requests.exeptions.ConnectionError:
		pass

file=open(file_name,'r')
for line in file:
	directory=line.strip()
	full_url= target_url+'/'+directory
	response=request(full_url)
	if response:
		print('[+] Discovered directory at this path '+ full_url)
