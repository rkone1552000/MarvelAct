import os
import hashlib
import json
import pandas as pd
from dotenv import load_dotenv
from Marvel_package_rin.createDF import createdf
from Marvel_package_rin.api import api_call

import urllib3
urllib3.disable_warnings()

load_dotenv(r'C:\Users\user\OneDrive\Desktop\MarvelCaseStudy\key.env')
privateKey = os.getenv('private_key')
publicKey = '2792447cd08dbb0f1fec94d6c5995dd5'
#print(privateKey)
ts = '2'

comb_val = ts+privateKey+publicKey
hash_val = hashlib.md5(comb_val.encode("utf-8")).hexdigest()

web_url = 'https://gateway.marvel.com:443/v1/public/characters'

namestartWith = input("Enter the character's first letter: ")

result = api_call(namestartWith, web_url, hash_val, publicKey, ts)

df = pd.DataFrame(result['data']['results'])
df.drop(df.columns[[2,3,4,5,10]], axis = 1, inplace=True)
print(df)


### Task continued in Activity3.py file
