#tronbal.py
#Tron Wallet Generator Check API for Balances/totalTransactionCount/frozen Ammount mizogg.co.uk 09/08/21
import ecdsa
import base58
import random
import requests
import json
import atexit
from time import time
from datetime import timedelta, datetime
from Crypto.Hash import keccak
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

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()

def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)

def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr

print(Fore.BLUE + "tronbal.py---" + Fore.RED + "Random Scan for TRON TRX Addresses Balances/totalTransactionCount/frozen Ammount----mizogg.co.uk"  + Style.RESET_ALL + seconds_to_str())
print(Fore.GREEN +"====================Starting search... Please Wait===================="+ Style.RESET_ALL)


count=0
while True:
    raw = bytes(random.sample(range(0, 256), 32))
    key = get_signing_key(raw)
    addr = verifying_key_to_addr(key.get_verifying_key()).decode()
    addhex = base58.b58decode_check(addr.encode()).hex()
    publickey = key.get_verifying_key().to_string().hex()
    privatekey = raw.hex()
    count+=1
    bloc = requests.get("https://apilist.tronscan.org/api/account?address=" + addr)
    res = bloc.json()
    balances = dict(res)["balance"] # balance balances tokenBalances transactions transactions_out totalFrozen
    transaction = dict(res)["totalTransactionCount"]
    frozen = dict(res)["totalFrozen"]
    print(Fore.BLUE + "trponbal.py---" + Fore.RED + "Random Scan for TRON TRX Addresses Balances/totalTransactionCount/frozen Ammount" + Style.RESET_ALL) 
    print (Fore.GREEN + 'TRON Address Random Scan : ' + Style.RESET_ALL + str (count) + ' : ' +Fore.RED + addr + Style.RESET_ALL) #TRON address display
    print(Fore.BLUE +'PrivateKey' + ' : ' + Fore.RED + privatekey + Style.RESET_ALL)
    print (Fore.YELLOW + ' --Balance = ' +  str(balances)+ '  --TotalFrozen  = ' +  str(frozen) + '  --Transactions = ' +  str(transaction) + Style.RESET_ALL)   
    print ("Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "-tronbal.py " + Style.RESET_ALL +" : Date&Time" + seconds_to_str(), '\n')
    if int(balances) > 0 or int(transaction) > 0 or int(frozen) > 0:
        print (Fore.GREEN+  ' <================================= WINNER TRON TRX WINNER =================================>' + '\n' +  Style.RESET_ALL)
        print(Fore.BLUE + "Matching Key ==== TRON address Found!!!\n PrivateKey: " + Style.RESET_ALL + privatekey) #TRON address winner
        print (Fore.BLUE + 'TRON Address Random Scan : ' + str (count) + ' : ' +Fore.GREEN + addr + Style.RESET_ALL)
        print (Fore.GREEN + ' --Balance = ' +  str(balances)+ '  --TotalFrozen  = ' +  str(frozen) + '  --Transactions = ' +  str(transaction) + Style.RESET_ALL) 
        print (Fore.GREEN+  ' <================================= WINNER TRON TRX WINNER =================================>' + '\n' +  Style.RESET_ALL)
        f=open(u"winner.txt","a")
        f.write('\n==========TRON TRX Address with Balances/totalTransactionCount/frozen Ammount==============')
        f.write('\nPrivateKey (hex) : ' + privatekey)
        f.write('\nPublic Key       : ' + publickey)
        f.write('\nTRON Address     : ' + addr)
        f.write('\nTRON Address(hex): ' + addhex)
        f.write('\n==========TRON TRX Address with Balances/totalTransactionCount/frozen Ammount==============')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====') 
        f.close()
        continue