import requests
root="F:/pictures/"
base_url = "http://10.10.64.6:8080/Common/GetPhotoByBH?xh="
for i in range(3150110001,3150931055):
	path = root + str(i)+ '.jpg'
	url = base_url + str(i)+'.jpg'
	r = requests.get(url)
	with open(path,'wb') as f:
		f.write(r.content)
