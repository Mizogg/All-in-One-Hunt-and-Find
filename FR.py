# FR.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address. Check for Final Balance/Transaction/Received Using blockchain.info API Request every 10 Seconds 09/08/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import itertools
from bit import *
from bit.format import bytes_to_wif
import random
import atexit
from time import time
from datetime import timedelta, datetime
from time import sleep
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

count=0
total=0

while True:
    try:
        ran= random.randint(x,y)
        key = Key.from_int(ran)
        seed=str(ran)
        wif = bytes_to_wif(key.to_bytes(), compressed=False)
        wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wif)
        caddr = key.address #Legacy compressed address
        uaddr = key1.address #Legacy uncompressed address
        saddr = key.segwit_address  #Segwit address
        query = {caddr}|{uaddr}|{saddr}
        request = requests.get("https://blockchain.info/multiaddr?active=" + ','.join(query), timeout=10)
        count+=1
        total+=3 
        try:
            request = request.json()
            print(Fore.BLUE + "\n FR.py ====== " + Fore.RED + "Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + " ====== FR.py" + Style.RESET_ALL)
            print ('\n ====== FR.py ====== ' + Fore.GREEN +  'Running Scan : ' + str (count) + '  :  ' + Fore.BLUE + 'Total Bitcoin Addresses : ' + str (total) + ' : ' + Fore.YELLOW + seconds_to_str() + '] --------------> '   + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (hex) : ' + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (dec) : ' + Fore.YELLOW + seed + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) Compressed : ' + Fore.YELLOW + wif2 + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) UnCompressed : ' + Fore.YELLOW + wif + Style.RESET_ALL)
            print (Fore.GREEN +  ' <================================= Bitcoin Addresses Checked for Final Balance/Transaction/Received  =================================>' + '\n' +  Style.RESET_ALL)

            #Parse results
            for row in request["addresses"]:
                print(row)
                if row["total_received"] > 0 or row["final_balance"] > 0 or row["n_tx"] > 0: # final_balance or n_tx or total_received or total_sent
                    print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey: " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
                    f=open(u"winner.txt","a")
                    f.write('\n=============Bitcoin Address with Final Balance/Transaction/Received Found=====================')
                    f.write('\nPrivateKey (hex): ' + key.to_hex())
                    f.write('\nBitcoin Address Compressed : ' + caddr)
                    f.write('\nBitcoin Address UnCompressed :' + uaddr)
                    f.write('\nBitcoin Segwit Address :' + saddr)
                    f.write('\nPrivateKey (wif) Compressed : ' + wif2)
                    f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
                    f.write('\n=============Bitcoin Address with Final Balance/Transaction/Received  Found=====================')
                    f.write('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' )
                    f.close()
                    continue
        except:
            pass
        sleep(10)
    except Exception as e:
        print(e)
        pass