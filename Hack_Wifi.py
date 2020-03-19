__author__="mojtaba.mcw"
import subprocess
shell_o = "netsh wlan show profiles"
file_obj = open('Access-Wifi.txt','w')
output = subprocess.check_output(shell_o.split(" ")).decode('utf-8').split('\n')
output = [i for i in output if "All User Profile" in i]
for i in output:
		w = i.split(':')[1].replace('\r','')
		w = w.strip()
		final = subprocess.check_output(['netsh','wlan','show','profiles',w,'key=clear']).decode('utf-8').split('\n')
		final = [b for b in final if "Key Content" in b]
		end = str(final).split("Key Content")[1].strip()
		file_obj.write(w+end+'\n')
		print (w,end)
file_obj.close()