#Mizogg 08/08/2021 Random Scan for Bitcoin Addresses and Balance Using BIT Library and API Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import random
import atexit
from time import time
from datetime import timedelta, datetime
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

print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

count=0
total=0
while True:
    ran= random.randint(1,115792089237316195423570985008687907852837564279074904382605163141518161494336)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address
    uaddr = key1.address
    bal = key.get_balance('btc')
    bal1 = key1.get_balance('btc')
    count+=1
    total+=2
    print(Fore.RED + '<== Current PrivateKey (dec) ==> ' + Fore.YELLOW + seed + Style.RESET_ALL)
    print (Fore.GREEN +  ' <================================= Bitcoin Addresses Checked for Balance =================================>' + '\n' +  Style.RESET_ALL)
    print(caddr + ' : ' + Fore.BLUE + key.to_hex() + ' : ' + Fore.YELLOW + wif2 + ' : ' + Fore.RED + bal + Style.RESET_ALL)
    print(uaddr + ' : ' + Fore.BLUE + key1.to_hex() + ' : ' + Fore.YELLOW + wif + ' : ' + Fore.RED + bal1 + Style.RESET_ALL)
    print (Fore.GREEN + "Scan Number" + ' : ' + Style.RESET_ALL + str (count) + ' : ' + Fore.GREEN + "Total Wallets Checked" + ' : ' + Style.RESET_ALL + str (total))
    print(Fore.BLUE + "---r2.py---" + Fore.RED + "Random Scan for Bitcoin Addresses and Check Balance---------mizogg.co.uk" + Fore.BLUE + "---r2.py--- "  + Style.RESET_ALL + seconds_to_str())
    if float (bal) or float (bal1) > 0:
        print (colour_purple +  ' <================================= WINNER WINNER WINNER WINNER =================================>' + '\n' +  Style.RESET_ALL)
        print (Fore.YELLOW + 'Congraz you have found wallet with a balance : ' + Style.RESET_ALL + caddr + Fore.GREEN + ' : Balance : ' + bal + Style.RESET_ALL)
        print (Fore.YELLOW + 'Congraz you have found wallet with a balance : ' + Style.RESET_ALL + uaddr +  Fore.GREEN +' : Balance : ' + bal1 + Style.RESET_ALL)
        print(Fore.RED + ' PrivateKey (wif) Compressed : ' + Fore.YELLOW + wif2 + Style.RESET_ALL)
        print(Fore.RED + ' PrivateKey (wif) UnCompressed : ' + Fore.YELLOW + wif + Style.RESET_ALL)
        print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
        print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + Fore.YELLOW + seed + Style.RESET_ALL)
        print('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' ) 
        print (colour_purple +  ' <================================= WINNER WINNER WINNER WINNER =================================>' + '\n' +  Style.RESET_ALL)
        f=open(u"winner.txt","a")
        f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr)
        f.write('\nBitcoin Address UnCompressed :' + uaddr)
        f.write('\nPrivateKey (wif) Compressed : ' + wif2)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
        f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
        f.write('\n Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ' ) 
        f.close()
        break