#!/usr/bin/python 
# -*- coding: utf-8 -*-

import md5
import os 
import hashlib
import subprocess
import time
import itertools, string
import hashlib
import sys
import signal
import threading

subprocess.call('clear', shell=True)
header = """                                                                                                                                
                                                                                                                                
        CCCCCCCCCCCCC                                                       kkkkkkkk           IIIIIIIIIITTTTTTTTTTTTTTTTTTTTTTT
     CCC::::::::::::C                                                       k::::::k           I::::::::IT:::::::::::::::::::::T
   CC:::::::::::::::C                                                       k::::::k           I::::::::IT:::::::::::::::::::::T
  C:::::CCCCCCCC::::C                                                       k::::::k           II::::::IIT:::::TT:::::::TT:::::T
 C:::::C       CCCCCCrrrrr   rrrrrrrrr   aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk  I::::I  TTTTTT  T:::::T  TTTTTT
C:::::C              r::::rrr:::::::::r  a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k   I::::I          T:::::T        
C:::::C              r:::::::::::::::::r aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k    I::::I          T:::::T        
C:::::C              rr::::::rrrrr::::::r         a::::ac:::::::cccccc:::::c k:::::k k:::::k     I::::I          T:::::T        
C:::::C               r:::::r     r:::::r  aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k      I::::I          T:::::T        
C:::::C               r:::::r     rrrrrrraa::::::::::::ac:::::c              k:::::::::::k       I::::I          T:::::T        
C:::::C               r:::::r           a::::aaaa::::::ac:::::c              k:::::::::::k       I::::I          T:::::T        
 C:::::C       CCCCCC r:::::r          a::::a    a:::::ac::::::c     ccccccc k::::::k:::::k      I::::I          T:::::T        
  C:::::CCCCCCCC::::C r:::::r          a::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k   II::::::II      TT:::::::TT      
   CC:::::::::::::::C r:::::r          a:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k  I::::::::I      T:::::::::T      
     CCC::::::::::::C r:::::r           a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k I::::::::I      T:::::::::T      
        CCCCCCCCCCCCC rrrrrrr            aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkkIIIIIIIIII      TTTTTTTTTTT      
                                                                                                                                
                                                                                                                                
"""
def main():
	print(header)
	print("1) Generate MD5")
	print("2) Bruteforce MD5 hash value")
	print("3) Password Attack MD5")
	print("")
	choice = raw_input("Enter the choice that you want: ")
	if choice == "1":
		encode = raw_input("Enter the text here ")
		h = hashlib.md5(encode.encode())
		h2 = h.hexdigest()
		print("MD5 hash value: ", h2)
		print("")
		con = raw_input("**Do you wish to continue:Y/N** ")
		if con == "Y":
			main()
		else:
			sys.exit()

	if choice == "2":
		done = False
		def signal_handler(signal, frame):
    			print 'You pressed Ctrl+C!'
    			global done
    			done=True
			sys.exit(0)
		def animate():
    			for c in itertools.cycle(['|', '/', '-', '\\']):
        			if done==True:
            				break
            
	        		sys.stdout.write('\rloading ' + c)
        			sys.stdout.flush()
				time.sleep(0.1)
		def _attack(chrs, inputt):
 			print "[+] Start Time: ", time.strftime('%H:%M:%S')
  	  		start_time = time.time()
    			t = threading.Thread(target=animate)
    			t.start()
  	  		total_pass_try=0
    			for n in range(1, 31+1):
      				characterstart_time = time.time()
      				print "\n[!] I'm at ", n , "-character"
      
      
  	   	 		for xs in itertools.product(chrs, repeat=n):
		
        		  		saved = ''.join(xs)
          				stringg = saved
          				m = hashlib.md5()
  	        			m.update(saved)
        	  			total_pass_try +=1
          				if m.hexdigest() == inputt:
              					time.sleep(10)
              					global done
              					done = True

  	            				print "\n[!] found ", stringg
        	      				print "\n[-] End Time: ", time.strftime('%H:%M:%S')
              					print "\n[-] Total Keyword attempted: ", total_pass_try
              					print("\n---Md5 cracked at %s seconds ---" % (time.time() - start_time))
						sys.exit("Thank You!")

      			print "\n[!]",n,"-character finished in %s seconds ---" % (time.time() - characterstart_time)
   			
			select = raw_input("Do you wish to continue:(Y/N) ")
			if select == "Y":
				brute_main()
			else:
				main()
		def brute_main():
			inp_usr = raw_input("Enter MD5 Hash value here: ")
    			chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    			print chrs
    			signal.signal(signal.SIGINT, signal_handler)
   		 	return _attack( chrs,inp_usr );
		brute_main()		

	if choice == "3":
		def crack():
			hash = raw_input("Enter the MD5 value: ")
			file = raw_input("Enter the password file location: ")
			with open(file,'r') as f:
				words = f.read().split()
			
			for word in words:
				word_hash = hashlib.md5(word).hexdigest()

				if word_hash == hash:
					return word

		def pass_main():
			password = crack()

			if password:
				print ('The password is `{0}`.'.format(password))

			else:
				print("The password can't be cracked")
			
			select = raw("Do you wish to continue:(Y/N) ")
			if select == "Y":
				pass_main()
			else:
				main()
		pass_main()

main()
