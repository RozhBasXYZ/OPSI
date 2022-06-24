import os,requests
try:ngr = requests.get("http://ip-api.com/json/").json();bas = ngr["country"]
except:bas = "Indonesia"
if __name__ == "__main__":
	if "Indonesia" == bas:
		os.system('git pull')
		__import__("opsi").menu()
	else:exit("sorry this script is only for Indonesian people")
