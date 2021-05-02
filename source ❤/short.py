# الاداة مجانية , للتعلم 
# اللهم انفعني بما علمتني، وعلمني ما ينفعني، وزدني علمًا
# IG : https://instagram.com/81111i
# Github: https://github.com/fzrael
# Discord: Fz#1111
# أي استفسار تواصل معي على الانستقرام

import random 
import requests 
import string
from os import system
system("title " + "FzRaeL - shortUrl - Open source -@81111i")

logo = '''

      _                _   _    _      _ 
     | |              | | | |  | |    | |
  ___| |__   ___  _ __| |_| |  | |_ __| |
 / __| '_ \ / _ \| '__| __| |  | | '__| |
 \__ \ | | | (_) | |  | |_| |__| | |  | |
 |___/_| |_|\___/|_|   \__|\____/|_|  |_|
                                         
                                         
'''
print(logo)

# سترينق عشوائي
def get_random_string(length):return (''.join(random.choice(string.ascii_lowercase) for i in range(length))+'_Fz')

url = input('shortUrl ==> : ')

#عدد الاسترينق 
strfz = get_random_string(3)

# إرسال الداتا witout API 
requests.post(
    'https://v.ht/processreq.php', 
data = {'txt_url': url,'txt_name': strfz}
)

print("URL ↓ \n"+"https://v.ht/"+strfz)
