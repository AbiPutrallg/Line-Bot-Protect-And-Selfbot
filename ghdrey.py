# -*- coding: utf-8 -*- 
from REYBOTS import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#sb ɢʜᴅ V.2.3.0
#rey_sᴇʙᴀsᴛɪᴀɴ_ɢʜᴅ
#jangan ᴜʙᴀʜ ᴍɪᴅ ᴄʀᴇᴀᴛᴏʀ
#remake ʙʏ: ʀᴇʏ_ɢʜᴅ
cl = LineClient() #Login via qr
#cl = LineClient("","") #login via email
#cl = LineClient(authToken='') #login via token
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))
print("Login SB GHD SUCCESS BANG REY")

poll = LinePoll(cl)
call = cl
creator = ["u411e5942b009ef65f26471d44843d9e2"]
owner = ["u411e5942b009ef65f26471d44843d9e2"]
admin = ["u411e5942b009ef65f26471d44843d9e2"]
mid = cl.getProfile().mid
Bots = [mid]
#==[tata letak sc ghd]==#
msg_dict = {}
msg_dict1 = {}

dt_to_str = {}
temp_flood = {}
welcome = []

#==[tata letak sc ghd]==#
settings = {
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "restartPoint": False,
    "userMentioned": False,
    "changeGroupPicture": [],
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "addfriend":False,
    "addfriend":{},
    "ContactSetting":{},
    "invite":False,
    "autoBlock":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "likeOn": True,
    "Timeline": True,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "autoJoin":True,
    "add":True,
    "autoAdd":False,
    "autoLeave":False,
    "autoLeave1":False,
    "autoread":False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "unsend":True,
    "sticker":False,
    "selfbot":True,
    "mention":"ᴏʏ ᴅᴇᴋ!! ɴɢɪɴᴛɪᴘ ᴍᴜʟᴜ sɪʜ.. \nsɪɴɪ ᴍᴀsᴜᴋ..😂",
    "Respontag":"jgn tag orang ganteng.. entar nafsu",
    "welcome":"ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ.. ᴘʟᴇᴀsᴇ ᴄᴇᴋ ɴᴏᴛ ᴀɴᴅ ᴘʟᴀʏ ᴠɪᴅᴇᴏ ɪɴ ɴᴏᴛ",
    "comment":"Ghd_Official hadir",
    "message":"thanks dah add aku kak.. hehe",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    owner = json.load(fp)    

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def backupData():
	try:
		backup = unsend
		f = codecs.open('unsend.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except Exception as error:
		logError(error)
		return False

def sendLineMusic(to):
    contentMetadata = {
        'countryCode': 'ID',
        'i-installUrl': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'a-packageName': 'com.spotify.music',
        'linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'type': 'mt',
        'previewUrl':"http://dl.profile.line-cdn.net/{}".format(client.profile.pictureStatus),
        'a-linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'text': cl.profile.displayName,
        'id': 'mt000000000a6b79f9',
        'subText': cl.profile.statusMessage
    }
    return cl.sendMessage(to, cl.profile.displayName, contentMetadata, 19)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╭────────────────╮\n│1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "│{}. ".format(str(no))
            else:
                textx += "\n│◈    「 {} 」\n╰────────────────╯".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴛᴏᴛᴀʟ sɪᴅᴇʀ「{}」\nᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ ᴡʀ. ᴡʙ. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ ɪɴ「{}」\nᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ ᴡʀ. ᴡʙ.  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionV2(to, text="", mids=[], name="", url="", iconlink=""):
    arrData = ""
    arr = []
    mention = "@yogi "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 9
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 9
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
  
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│" + key + "ᴍᴇ\n" + \
                  "│" + key + "ᴍɪᴅ「@」\n" + \
                  "│" + key + "ɪɴғᴏ「@」\n" + \
                  "│" + key + "ᴍʏʙᴏᴛ\n" + \
                  "│" + key + "sᴛᴀᴛᴜs\n" + \
                  "│" + key + "ᴀʙᴏᴜᴛ\n" + \
                  "│" + key + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "│" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "│" + key + "ᴄʀᴇᴀᴛᴏʀ\n" + \
                  "│" + key + "sᴘᴇᴇᴅ/sᴘ\n" + \
                  "│" + key + "sᴘʀᴇsᴘᴏɴ\n" + \
                  "│" + key + "ʙᴜᴛ/ʙᴏs\n" + \
                  "│" + key + "ʙʏᴇᴍᴇ\n" + \
                  "│" + key + "ʟᴇᴀᴠᴇ「ɴᴀᴍᴇ」\n" + \
                  "│" + key + "ɢɪɴғᴏ\n" + \
                  "│" + key + "ᴄʟᴏɴᴇ @\n" + \
                  "│" + key + "ʀᴇsᴛᴏʀᴇ\n" + \
                  "│" + key + "ᴏᴘᴇɴ\n" + \
                  "│" + key + "ᴄʟᴏsᴇ\n" + \
                  "│" + key + "ᴜʀʟ ɢʀᴜᴘ\n" + \
                  "│" + key + "ɢʀᴜᴘʟɪsᴛ\n" + \
                  "│" + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n" + \
                  "│" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "│" + key + "ᴄʟᴇᴀʀ\n" + \
                  "│" + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ʟᴜʀᴋᴇʀs\n" + \
                  "│" + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴜᴘᴅᴀᴛᴇғᴏᴛᴏ\n" + \
                  "│" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "│" + key + "ʙʀᴏᴀᴅᴄᴀsᴛ:「ᴛᴇxᴛ」\n" + \
                  "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│✧ᴺᴼʙᴀᴘᴇʀ__ᴺᴼsᴀɴɢᴇᴺᴼ  ✧" + "\n" + \
                  "│✧ᴄᴏᴘʏʀɪɢʜᴛ:ɢʜᴅ selfbot✧" + "\n" + \
                  "╰────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╯"
    return helpMessage

def public():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│" + key + "sᴇᴛᴋᴇʏ「ᴋᴇʏ」\n" + \
                  "│" + key + "ᴍʏᴋᴇʏ\n" + \
                  "│" + key + "ʀᴇsᴇᴛᴋᴇʏ\n" + \
                  "│" + key + "ᴛᴀғsɪʀǫᴜʀᴀɴ\n" + \
                  "│" + key + "ᴄᴠᴘ\n" + \
                  "│" + key + "ɪᴅ ʟɪɴᴇ:「ɪᴅ」\n" + \
                  "│" + key + "sʜᴏʟᴀᴛ:「ᴋᴏᴛᴀ」\n" + \
                  "│" + key + "ᴄᴜᴀᴄᴀ:「ᴋᴏᴛᴀ」\n" + \
                  "│" + key + "ʟᴏᴋᴀsɪ:「ᴋᴏᴛᴀ」\n" + \
                  "│" + key + "ᴍᴜsɪᴄ:「ᴊᴜᴅᴜʟ」\n" + \
                  "│" + key + "ʟɪʀɪᴋ:「ᴊᴜᴅᴜʟ」\n" + \
                  "│" + key + "ᴍᴘ3「ᴊᴜᴅᴜʟ」\n" + \
                  "│" + key + "ʏᴛᴍᴘ4:「ᴊᴜᴅᴜʟ」\n" + \
                  "│" + key + "ᴘʀᴏғɪʟɪɢ:「ɴᴀᴍᴇ」\n" + \
                  "│" + key + "ᴄᴇᴋᴅᴀᴛᴇ:「ᴛɢʟ-ʙʟɴ-ᴛʜ」\n" + \
                  "│" + key + "ᴊᴜᴍʟᴀʜ:「ɴᴏ」\n" + \
                  "│" + key + "sᴘᴀᴍᴛᴀɢ「@」\n" + \
                  "│" + key + "sᴘᴀᴍᴄᴀʟʟ:「ᴊᴜᴍʟᴀʜ」\n" + \
                  "│" + key + "sᴘᴀᴍᴄᴀʟʟ\n" + \
                  "│" + key + "ʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴡᴇʟᴄᴏᴍᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "sᴘᴀᴍɪɴᴠɪᴛᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴜɴsᴇɴᴅ「ᴏɴ/ᴏғғ」\n" + \
                  "│" + key + "ᴛɪᴍᴇʟɪɴᴇ「ᴏɴ/ᴏғғ」\n" + \
                  "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│✧ᴺᴼʙᴀᴘᴇʀ__ᴺᴼsᴀɴɢᴇᴺᴼ  ✧" + "\n" + \
                  "│✧ᴄᴏᴘʏʀɪɢʜᴛ:ɢʜᴅ selfbot✧" + "\n" + \
                  "╰────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╯"
    return helpMessage1

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│" + key + "ᴄᴇᴋ sɪᴅᴇʀ\n" + \
                  "│" + key + "ᴄᴇᴋ sᴘᴀᴍ\n" + \
                  "│" + key + "ᴄᴇᴋ ᴘᴇsᴀɴ\n" + \
                  "│" + key + "ᴄᴇᴋ ʀᴇsᴘᴏɴ\n" + \
                  "│" + key + "ᴄᴇᴋ ᴡᴇʟᴄᴏᴍᴇ\n" + \
                  "│" + key + "sᴇᴛ sɪᴅᴇʀ:「ᴛᴇxᴛ」\n" + \
                  "│" + key + "sᴇᴛ sᴘᴀᴍ:「ᴛᴇxᴛ」\n" + \
                  "│" + key + "sᴇᴛ ᴘᴇsᴀɴ:「ᴛᴇxᴛ」\n" + \
                  "│" + key + "sᴇᴛ ʀᴇsᴘᴏɴ:「ᴛᴇxᴛ」\n" + \
                  "│" + key + "sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:「ᴛᴇxᴛ」\n" + \
                  "│" + key + "ɴᴀᴍᴇ:「ɴᴀᴍᴇ」\n" + \
                  "│" + key + "ɢɪғᴛ:\n" + \
                  "│" + key + "sᴘᴀᴍ:\n" + \
                  "│" + key + "sᴘᴀᴍɪɴᴠɪᴅ|ᴜsᴇʀ|ᴊᴍʟʜ|ɴᴀᴍᴇ\n" + \
                  "╰───────┳─┳────────╯" + "\n" + \
                  "╭───────┻─┻────────╮" + "\n" + \
                  "│✧ᴺᴼʙᴀᴘᴇʀ_ᴺᴼsᴀɴɢᴇᴺᴼᴜʜ✧" + "\n" + \
                  "│✧ᴄᴏᴘʏʀɪɢʜᴛ:ɢʜᴅ selfbot✧" + "\n" + \
                  "╰────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╯"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"ᴀᴋᴜ ᴘᴀᴍɪᴛ ᴅʟᴜ sᴀʏ\nɢʀᴜᴘ: " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"ᴀᴋᴜ ᴅᴀᴛᴀɴɢ ʟᴀɢɪ " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"ᴀᴋᴜ ᴅᴀᴛᴀɴɢ ʟᴀɢɪ " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"ᴀᴋᴜ ᴅᴀᴛᴀɴɢ ʟᴀɢɪ " + str(ginfo.name))

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 0:
            return
        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.findAndAddContactsByMid(op.param1)
                  sendMention1(op.param1, op.param1, "ʜʏ ᴋᴀᴋ ", ", ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ")
                  cl.sendText(op.param1, wait["message"])
                  cl.sendContact(op.param1, "u411e5942b009ef65f26471d44843d9e2")

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

#====================================================================
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)                                
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.createGroup("n̸͟͞o̸͟͞ b̸͟͞a̸͟͞p̸͟͞e̸͟͞r̸͟͞ n̸͟͞o̸͟͞ a̸͟͞n̸͟͞g̸͟͞e̸͟͞ u̸͟͞h̸͟͞h̸͟͞",[target]) 
                                cl.createGroup("m̸͟͞e̸͟͞n̸͟͞c̸͟͞i̸͟͞n̸͟͞t̸͟͞a̸͟͞i̸͟͞m̸͟͞u̸͟͞ s̸͟͞a̸͟͞y̸͟͞ u̸͟͞h̸͟͞h̸͟͞h̸͟͞",[target])
                                cl.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                settings['SpamInvite'] = False
                            except:             
                                 cl.sendMessage(msg.to, 'Contact error')
                                 settings['SpamInvite'] = False
                                 break



#===================================================================================================        
        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)                        
                    
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nsᴛɪᴄᴋᴇʀ ɪɴғᴏ"
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇ: {}".format(pkg_id)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴜʀʟ: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nsᴛɪᴄᴋᴇʀ ɪɴғᴏ"
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴘᴋɢ: {}".format(pkg_id)
                   ret_ += "\nsᴛɪᴄᴋᴇʀ ᴜʀʟ: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           rnd = ["Anjay tag mulu elu mah! rey cipok bunting elu."]
                           p = random.choice(rnd)
                           lang = 'id'
                           tts = gTTS(text=p, lang=lang)
                           tts.save("hasil.mp3")
                           cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"51626511","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "╔──────────────────╗\n│✮│ ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴀᴋᴜ sᴀʏ..\n│✮│ɴᴛᴀʀ ᴋᴀᴍᴜ ᴀɴɢᴇ ʟʜᴏ\n╚────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╝")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendReplyMessage(msg.id,msg.to,"╔──────────────────╗\n│✮│ 「ᴄᴇᴋ ɪᴅ sᴛɪᴄᴋᴇʀ」\n│✮│sᴛᴋɪᴅ: " + msg.contentMetadata["STKID"] + "\n│✮│sᴛᴋᴘᴋɢɪᴅ: " + msg.contentMetadata["STKPKGID"] + "\n│✮│sᴛᴋᴠᴇʀ: " + msg.contentMetadata["STKVER"]+ "\n│✮│「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\n│✮│line://shop/detail/" + msg.contentMetadata["STKPKGID"] + "╚────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╝")

               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╔──────────────────╗\n│✮│ ɴᴀᴍᴀ: " + msg.contentMetadata["displayName"] + "\n│✮│ᴍɪᴅ: " + msg.contentMetadata["mid"] + "\n│✮│sᴛᴀᴛᴜs ᴍsɢ: " + contact.statusMessage + "\n│✮│ᴘɪᴄᴛᴜʀᴇ ᴍsɢ: http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n╚────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╝")
                        cl.sendImageWithURL(msg.to, image)
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.likePost(url[25:58], url[66:], likeType=1001)
                     cl.createComment(url[25:58], url[66:], wait["comment"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n sᴛɪᴄᴋᴇʀ ɢʜᴅ ɪɴғᴏ "
                   ret_ += "\n sᴛᴋɪᴅ: {}".format(stk_id)
                   ret_ += "\n sᴛᴋᴠᴇʀ: {}".format(stk_ver)
                   ret_ += "\n sᴛᴋᴘᴋɢɪᴅ: {}".format(pkg_id)
                   ret_ += "\n sᴛᴋᴜʀʟ: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendReplyMessage(msg.id,msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendReplyMessage(msg.id,msg.to,"  ɢʜᴅ ᴄᴏɴᴛᴀᴄᴛ ɪɴғᴏ\n ɴᴀᴍᴇ: " + msg.contentMetadata["displayName"] + "\n ᴍɪᴅ: " + msg.contentMetadata["mid"] + "\n sᴛᴀᴛᴜs ᴍsɢ: " + contact.statusMessage + "\n ɪᴍᴀɢᴇ ᴜʀʟ: http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "Maaf, dia ada di daftar blacklist\n")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "Ketik invite off jika sudah masuk"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendReplyMessage(msg.id,msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendMessage(msg.to,"ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʟɪᴍɪᴛ")
                                  wait["invite"] = False
                                  break
#UPDATE FOTO
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")

               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴀᴅᴅɪɴɢ ɪᴍᴀɢᴇs {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴀᴅᴅɪɴɢ ᴠɪᴅᴇᴏs {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴀᴅᴅɪɴɢ sᴛɪᴄᴋᴇʀs {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴀᴅᴅɪɴɢ ᴍᴜsɪᴄ {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴄʜᴀɴɢᴇ ɪᴍᴀɢᴇ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["foto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(,msg.to,"ɪᴍᴀɢᴇ sᴜᴄᴄᴇss ᴄʜᴀɴɢᴇ")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              sendMention1(msg.to, sender, "「 ɢʜᴅ ʀᴇsᴜʟᴛ ᴠɪᴅᴇᴏs 」\nsᴇʟᴀᴍᴀᴛ ᴍᴇɴɪᴋᴍᴀᴛɪ ᴋᴀᴋ ", "\nᴡᴀɪᴛɪɴɢ ᴘʀᴏɢʀᴇss ᴠɪᴅᴇᴏs..")
                              cl.sendVideo(msg.to, videos[video])
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              sendMention1(msg.to, sender, "「 ɢʜᴅ ʀᴇsᴜʟᴛ ᴍᴘ3 」\nsᴇʟᴀᴍᴀᴛ ᴍᴇɴɪᴋᴍᴀᴛɪ ᴋᴀᴋ ", "\nᴡᴀɪᴛɪɴɢ ᴘʀᴏɢʀᴇss ᴀᴜᴅɪᴏs..")
                              cl.sendAudio(msg.to, audios[audio])
                        cmd = command(text)
                        if cmd == "ghd":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                veza = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│✮sᴇʟғʙᴏᴛ ɢʜᴅᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ ɢʜᴅ: "
                                ret_ = str(helpMessage)
                                ry = str(veza.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendReplyMessage(msg.id,msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "sᴇʟғ ɢʜᴅ ᴅɪᴀᴋᴛɪғᴋᴀɴ")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "sᴇʟғ ɢʜᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                                            
                        if cmd == "ghd2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage1 = public()
                                veza = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│✮sᴇʟғʙᴏᴛ ɢʜᴅᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ ɢʜᴅ: "
                                ret_ = str(helpMessage1)
                                ry = str(veza.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        if cmd == "ghd3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage2 = helpbot()
                                veza = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│✮sᴇʟғʙᴏᴛ ɢʜᴅᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ ɢʜᴅ: "
                                ret_ = str(helpMessage2)
                                ry = str(veza.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        if cmd == "ghd4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage3 = helpgroup()
                                veza = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│✮sᴇʟғʙᴏᴛ ɢʜᴅᴮᴼᵀʟɪɴᴇ✯\n│✯ᴜsᴇʀ ɢʜᴅ: "
                                ret_ = str(helpMessage3)
                                ry = str(veza.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':veza.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┝────────────────\n"
                                if wait["sticker"] == True: md+="│sᴛɪᴄᴋᴇʀ「🔲」\n"
                                else: md+="│sᴛɪᴄᴋᴇʀ「🔳」\n"
                                if wait["contact"] == True: md+="│🔰ᴄᴏɴᴛᴀᴄᴛ「🔲」\n"
                                else: md+="│ᴄᴏɴᴛᴀᴄᴛ「🔳」\n"
                                if wait["detectMention"] == True: md+="│🔰ʀᴇsᴘᴏɴ「🔲」\n"
                                else: md+="│ʀᴇsᴘᴏɴ「🔳」\n"
                                if wait["autoJoin"] == True: md+="│🔰ᴀᴜᴛᴏᴊᴏɪɴ「🔲」\n"
                                else: md+="│ᴀᴜᴛᴏᴊᴏɪɴ「🔳」\n"
                                if wait["autoAdd"] == True: md+="│🔰ᴀᴜᴛᴏᴀᴅᴅ「🔲」\n"
                                else: md+="│ᴀᴜᴛᴏᴀᴅᴅ「🔳」\n"
                                if msg.to in welcome: md+="│🔰ᴡᴇʟᴄᴏᴍᴇ「🔲」\n"
                                else: md+="│ᴡᴇʟᴄᴏᴍᴇ「🔳」\n"
                                if wait["autoLeave"] == True: md+="│🔰ᴀᴜᴛᴏʟᴇᴀᴠᴇ「🔲」\n"
                                else: md+="│ᴀᴜᴛᴏʟᴇᴀᴠᴇ「🔳」\n"
                                ginfo = cl.getGroup(msg.to)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭──────────────────╮\n│「 sᴇᴛ user」\n│♠ pemakai: "
                                ret_ = "│♠ ɢʀᴏᴜᴘ: {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "┝────────────────\n│♠ ɢʜᴅ ᴄʟᴏᴄᴋ: 「"+ datetime.strftime(timeNow,'%H:%M:%S')+"」 "+"\n│♠ ɢʜᴅ ᴅᴀᴛᴇ: 「"+ datetime.strftime(timeNow,'%Y-%m-%d') +"」\n╰────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╯"
                                cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to,"🔳🔳ᴄʀᴇᴀᴛᴏʀ ᴳᴴᴰᴢᴏʀᴅsˢᴱᴸᶠ🔲🔲") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 ᴛʏᴘᴇ sᴇʟғʙᴏᴛ」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendContact(to, sender)
                               sendMention(to, "╭────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╮\n│✆「sᴇʟғ ᴠ.9.3.0」 \n│✆「ᴛʏᴘᴇ ᴳᴴᴰʀᴇʏ.s」 \n│✆「ᴄᴏᴍᴇ ᴏɴ ᴏʀᴅᴇʀ」 \n│✆「ᴡᴇ ᴀʀᴇ ɢʜᴅ°ᴮᴼᵀ」\n│✆「ᴜsᴇʀ: @! 」\n╰────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╯",[sender])

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'salam':
                               cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'assalamualaikum':
                               cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'waalaikumsalam':
                               cl.sendMessage(msg.to, "ُиαн gιтυ ∂σик кαк.. кαℓαυ α∂α уαиg ѕαℓαм ∂ι ʝαωαв.. тєяιмα кαѕιн кαк")

                        elif cmd == "kenizawa" or text.lower() == 'ghdbot':
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 rey = "ᴳᴴᴰᴋᴇɴɪᴢᴀᴡᴀ 「ケニザワ」\nᵀᴱᴬᴹɢʜᴅ sᴇʟғʙᴏᴛ"
                                 rey += "\n\n" + datetime.strftime(timeNow,'%d-%m-%Y')
                                 rey += " " + datetime.strftime(timeNow,'%H:%M:%S')
                                 contact = cl.getContact(msg._from)
                                 cl.sendMessage(to, rey)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "╔──────────────────╗\n│🔰ɴᴀᴍᴇ: "+str(mi.displayName)+"\n│🔰ᴍɪᴅ: " +key1+ "\n╚────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╝")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "╔──────────────────╗\n│🔰ɴᴀᴍᴇ: "+str(mi.displayName)+"\n│🔰ᴍɪᴅ: " +key1+"\n│🔰sᴛᴀᴛᴜs"+str(mi.statusMessage)+"\n╚────ஜ۩ʀᴇʏ_ᴍɪᴀ۩ஜ─────╝")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "clear":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to, "🔳sᴜᴄᴄᴇss ʀᴇsᴇᴛ ᴄʜᴀᴛ🔳")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[🔳ɢʜᴅ sʜᴀʀᴇ🔲]\n" + str(pesan))

                        elif cmd.startswith("gb: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bctxt = cmd.replace("gb: ", "")
                                a = cl.getGroupIdsJoined()
                                me = cl.getProfile()
                                name = "ʙʀᴏᴀᴅᴄᴀsᴛ ɢʀᴏᴜᴘ"
                                url = 'https://line.me/ti/p/{}'.format(str(cl.getUserTicket().id))
                                iconlink = "http://dl.profile.line-cdn.net/{}".format(str(me.pictureStatus))
                                cl.sendMessage(to, "sᴜᴄᴄᴇss ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴ: "+str(len(a))+" ɢʀᴏᴜᴘ")
                                for manusia in a:
                                    C = cl.getContact(mid)
                                    mids = [C.mid]
                                    text = "{}\n「ɢʜᴅ ʙᴄ」\nɢʜᴅ: @!".format(str(bctxt))
                                    sendMentionV2(manusia, text, mids,str(name),str(url),str(iconlink))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「🔲ᴍʏᴋᴇʏ🔳」\nᴍʏ sᴇᴛᴋᴇʏ sᴇʟғ「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "ɢᴀɢᴀʟ ᴄʜᴀɴɢᴇ sᴇᴛᴋᴇʏ")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「🔲sᴇᴛᴋᴇʏ🔳」\nsᴇᴛᴋᴇʏ ᴄʜᴀɴɢᴇ ᴛᴏ「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「🔳sᴇᴛᴋᴇʏ🔲」\n ᴍʏ sᴇᴛᴋᴇʏ ᴡɪʟʟ ʙᴇ ʀᴇsᴇᴛ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender,"╔────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╗\n│ᴡᴀɪᴛing ʙᴏss..\n│ᴘʀᴏɢʀᴇss ʀᴇsᴛᴀʀᴛ\n│ᴜsᴇʀ: ", " \n│ °ɢʜᴅ ʀᴇsᴛᴀʀᴛ° ᴅᴏɴᴇ°\n╚────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╝")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "「sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴋᴇᴍʙᴀʟɪ sᴀʏ」")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏᴛʜɪɴɢ"
                                else:
                                    gQr = "ᴏᴘᴇɴᴇᴅ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "ɢʜᴅ sᴇʟғ ɢʀᴜᴘ ɪɴғᴏ\nɴᴀᴍᴀ ɢʀᴏᴜᴘ: {}".format(G.name)+ "\nɪᴅ ɢʀᴏᴜᴘ: {}".format(G.id)+ "\nᴘᴇᴍʙᴜᴀᴛ: {}".format(G.creator.displayName)+ "\nᴡᴀᴋᴛᴜ ᴛᴇʙᴜᴀᴛ: {}".format(str(timeCreated))+ "\nᴊᴜᴍʟᴀʜ ᴊᴀɴᴅᴀ: {}".format(str(len(G.members)))+ "\nᴊᴜᴍʟᴀʜ ᴅᴜᴅᴀ: {}".format(gPending)+ "\nɢʀᴏᴜᴘ ǫʀ: {}".format(gQr)+ "\nɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ: {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "ɢʜᴅ ʙᴏᴛ ɪɴғᴏ ɢʀᴜᴘ\n"
                                ret_ += "\nɴᴀᴍᴇ ɢʀᴏᴜᴘ: {}".format(G.name)
                                ret_ += "\nɪᴅ ɢʀᴏᴜᴘ: {}".format(G.id)
                                ret_ += "\nᴄʀᴇᴀᴛᴏʀ: {}".format(gCreator)
                                ret_ += "\nᴛɪᴍᴇ ᴄʀᴇᴀᴛᴇ: {}".format(str(timeCreated))
                                ret_ += "\nʟɪsᴛ ᴀɴɢɢᴏᴛᴀ: {}".format(str(len(G.members)))
                                ret_ += "\nʟɪsᴛ ᴘᴇɴᴅɪɴɢ: {}".format(gPending)
                                ret_ += "\nɢʀᴏᴜᴘ ǫʀ: {}".format(gQr)
                                ret_ += "\nɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ: {}".format(gTicket)
                                ret_ += "ɪɴғᴏ ɢʀᴏᴜᴘ ʙʏ ɢʜᴅ sᴇʟғ"
                                cl.sendMessage(msg.to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"ɢʀᴏᴜᴘ ɴᴀᴍᴇ: [ " + str(G.name) + " ]\n\n   [ ʟɪsᴛ ᴍᴇᴍʙᴇʀ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("out "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ ɢʜᴅ ғʀɪᴇɴᴅ ʟɪsᴛ ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ ɢʜᴅ ɢʀᴏᴜᴘ ʟɪsᴛ ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ᴜʀʟ ᴡɪʟʟ ᴏᴘᴇɴᴇᴅ")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ᴜʀʟ ᴡɪʟʟ ᴄʟᴏsᴇ")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ɴᴀᴍᴇ: "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ: http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ sᴀʏ")
              
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                cl.sendMessage(msg.to,"ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ sᴀʏ")

                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"ɴᴀᴍᴇ " + string + "")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                cl.sendMessage(msg.to,"ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ʙᴏss")
                                
                        elif cmd.startswith("cvp: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                cl.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                cl.sendMessage(msg.to, "ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ɪᴍᴀɢᴇ ʙᴏs")

#====================================================================   
                        elif 'like ' in text.lower():
                           if msg._from in admin:
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(msg.to), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(msg.to), str(result), wait["comment"])
                                    cl.sendMessage(msg.to, 'ɢʜᴅ ᴅᴏɴᴇ ʟɪᴋᴇ ᴀɴᴅ ᴄᴏᴍᴍᴇɴᴛ '+str(len(st))+' ᴘᴏsᴛ ғʀᴏᴍ' + str(s))
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("image "):
                            text_ = removeCmd("imagetext", text)
                            web = _session
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            font = random.choice(["arial","comic"])
                            r = web.get("http://api.img4me.com/?text=%s&font=%s&fcolor=FFFFFF&size=35&bcolor=000000&type=jpg" %(urllib.parse.quote(text_),font))
                            data = str(r.text)
                            if "Error" not in data:
                                path = data
                                cl.sendImageWithURL(to,path)
                            else:
                                cl.sendMessage(to,"[RESULT] %s" %(data.replace("Error: ")))

#===========BOT UPDATE============#
                        elif cmd == "but" or text.lower() == 'bos':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "ʙʏᴇ ɢʀᴏᴜᴘ ᴋᴇsᴀʏᴀɴɢᴀɴᴋᴜ "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "ɢʜᴅ sᴘᴇᴇᴅ ʀᴇsᴘᴏɴ\n\n - ɢᴇᴛ ᴘʀᴏғɪʟᴇ:\n%.10f\n - ɢᴇᴛ ᴄᴏɴᴛᴀᴄᴛ:\n%.10f\n - ɢᴇᴛ ɢʀᴏᴜᴘ\n%.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               sendMention1(msg.to, sender, "⇨sᴘᴇᴇᴅ ᴜᴘ\nᴜsᴇʀ:","")
                               start = time.time() 
                               time.sleep(0.002)  
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to,format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ᴡɪʟʟ ʙᴇ ᴀᴋᴛɪғ\nᴛᴀɴɢɢᴀʟ: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ: [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ᴡɪʟʟ ʙᴇ ᴏғғ\nᴛᴀɴɢɢᴀʟ: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ: [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nᴛᴀɴɢɢᴀʟ: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ: [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "ᴜsᴇʀ ᴋᴏsᴏɴɢ..")
                            else:
                                cl.sendMessage(msg.to, "ᴋᴇᴛɪᴋ ʟᴜʀᴋɪɴɢ ᴏɴ ᴘʟᴇᴀsᴇ..")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "╔────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╗\n│  🔳ᴄᴇᴋ sɪᴅᴇʀ ɢʜᴅ ᴏɴ🔲\n┝───────────────────\n│🔳ᴛᴀɴɢɢᴀʟ: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│🔲ᴊᴀᴍ:  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╝")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "╔────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╗\n│ 🔳ᴄᴇᴋ sɪᴅᴇʀ ɢʜᴅ ᴏғғ🔲\n┝───────────────────\n│🔳ᴛᴀɴɢɢᴀʟ: "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│🔲ᴊᴀᴍ:  "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╝")
                              else:
                                  cl.sendMessage(msg.to, "sᴜᴅᴀʜ ᴏғғ ʙᴏs")

#===========Hiburan============#
                        elif cmd.startswith("post "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            post = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("http://m.jancok.com/klik/{}/".format(urllib.parse.quote(post)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = '「 Get Postingan 」\n\n'
                                try:
                                    for title in soup.select("[class~=badge-item-title]"):
                                        ret_ += "• Judul : "+title.get_text()
                                        ret_ += "\n• Link : m.jancok.com"
                                    for link in soup.find_all('img',limit=1):
                                        cl.sendMessage(msg.to, ret_)
                                        cl.sendImageWithURL(msg.to, link.get('src'))
                                except Exception as e:
                                    cl.sendMessage(msg.to, "Post kosong")
                                    print(str(e))

                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "sᴜʙᴜʜ: " and data[2] != "ᴅᴢᴜʜᴜʀ: " and data[3] != "ᴀsʏᴀʀ: " and data[4] != "ᴍᴀɢʀɪʙ: " and data[5] != "ɪsʏᴀ: ":
                                         ret_ = "「ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ」"
                                         ret_ += "\nʟᴏᴋᴀsɪ: " + data[0]
                                         ret_ += "\n" + data[1]
                                         ret_ += "\n" + data[2]
                                         ret_ += "\n" + data[3]
                                         ret_ += "\n" + data[4]
                                         ret_ += "\n" + data[5]
                                         ret_ += "\n\nᴛᴀɴɢɢᴀʟ: " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nᴊᴀᴍ: " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("tafsirquran "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        cl.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n"+data.findAll('p')[1].text
                                                    cl.sendMessage(msg.to, str(ret))
                                                except:
                                                    cl.sendMessage(msg.to, "Gagal mengambil data.") 

                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(0.1)
                                cl.sendMessage(msg.to, "ɪᴅ sᴍᴜʟᴇ: "+smule+"\nʟɪɴᴋ: "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                          
                        elif msg.text.lower().startswith("smule: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("https://citldesign.herokuapp.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                cl.sendImageWithURL(msg.to, image)
                                cl.sendAudioWithURL(msg.to, url)
                                cl.sendVideoWithURL(msg.to, url)
                                
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)                            
                                                                
                        elif cmd.startswith("getmeme"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "Meme image list\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    cl.sendMessage(msg.to,hasil)
                                    sendMention(msg.to,"@!\nsɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴋᴇɪɴɢɪɴᴀɴ:\n\n[Cek meme]\ngetmeme | urutan\n\n[Create meme]\nmeme teks1|teks2|urutan",[sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        sendMention(msg.to, sender,"","\nfoto sedang diproses...")
                                        cl.sendMessage(msg.to,hasil)
                                        cl.sendImageWithURL(msg.to,gambar["url"])
                                    except Exception as e:
                                        cl.sendMessage(msg.to," "+str(e))
                        elif "meme" in text.lower():
          #                 if msg._from admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                    result = api.caption_image(meme, atas,bawah)
                                    sendMention(msg.to, msg._from,"","\nfoto sedang diproses...")
                                    cl.sendImageWithURL(msg.to,result["url"])
                                except Exception as e:
                                    cl.sendMessage(msg.to," "+str(e)) 

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「sᴛᴀᴛᴜs ᴄᴜᴀᴄᴀ」"
                                    ret_ += "\nʟᴏᴋᴀsɪ: " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nsᴜʜᴜ: " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\nᴋᴇʟᴇᴍʙᴀʙᴀɴ: " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\nᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ: " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\nᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ: " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nᴛᴀɴɢɢᴀʟ: " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nᴊᴀᴍ: " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「ɪɴғᴏ ʟᴏᴋᴀsɪ」"
                                    ret_ += "\nʟᴏᴋᴀsɪ: " + data[0]
                                    ret_ += "\nɢᴏᴏɢʟᴇ ᴍᴀᴘs: " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendReplyMessage(msg.id,msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ ʟʏʀɪᴄ]"
                                          ret_ += "\n╠ ɴᴀᴍᴇ sᴏɴɢ: {}".format(str(song[0]))
                                          ret_ += "\n╠ ᴅᴜʀᴀᴛɪᴏɴ: {}".format(str(song[1]))
                                          ret_ += "\n╠ ʟɪɴᴋ: {}".format(str(song[3]))
                                          ret_ += "\n╚══[ ғɪɴɪsʜ ]\n\nʟɪʀɪᴋɴʏᴀ:\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendReplyMessage(msg.id,msg.to, "ʟɪʀɪᴋ ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ")

                        elif cmd.startswith("get-apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = " sᴇᴀʀᴄʜɪɴɢ ᴀᴘʟɪᴄᴀᴛɪᴏɴ\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "ɴᴇxᴛ ᴋʟɪᴋ:\nɢᴇᴛ-ᴀᴘᴋ {} | ᴀɴɢᴋᴀ".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendReplyMessage(msg.id,msg.to,ret_)

                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「ɢᴏᴏɢʟᴇ ɪᴍᴀɢᴇ」\nᴛʏᴘᴇ: sᴇᴀʀᴄʜ ɪᴍᴀɢᴇ\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ: %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "ᴊᴜᴅᴜʟ [ " + vid.title + " ]"
                                    author = '\n\nᴀᴜᴛʜᴏʀ: ' + str(vid.author)
                                    durasi = '\nᴅᴜʀᴀᴛɪᴏɴ: ' + str(vid.duration)
                                    suka = '\nʟɪᴋᴇs: ' + str(vid.likes)
                                    rating = '\nʀᴀᴛɪɴɢ: ' + str(vid.rating)
                                    deskripsi = '\nᴅᴇsᴋʀɪᴘsɪ: ' + str(vid.description)
                                sendMention1(msg.to, sender,"╔────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╗\n│ᴡᴀɪᴛɪɴɢ ʙᴏss..\n│ᴘʀᴏɢʀᴇss ʏᴍᴘ4\n│ᴜsᴇʀ: ", " \n│ °ɢʜᴅ ᴜsᴇ° ᴠɪᴅᴇᴏs°\n╚────ஜ۩ɢʜᴅ_sᴇʟғ۩ஜ─────╝")
                                cl.sendVideoWithURL(msg.to, me)
                    #            cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.id,msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "Link : " + "https://www.instagram.com/" + instagram
                                text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"I N F O R M A S I \n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴛᴀɢ ᴄʜᴀɴɢᴇ ᴛᴏ " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴄʜᴀɴɢᴇ ᴛᴏ " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        sendMention1(msg.to, sender,"sᴘᴀᴍ ᴍᴇʟᴇʙɪʜɪ ʙᴀᴛᴀs  ", " \n sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ ʙᴀᴛᴀs")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    cl.sendMessage(msg.to,"@! sᴜᴋsᴇs sᴘᴀᴍ ɢʀᴏᴜᴘ!\n\nᴜsᴇʀɪᴅ: @!\nᴊᴜᴍʟᴀʜ: {}\nɴᴀᴍᴇ ɢʀᴏᴜᴘ: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    dhenza = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  " ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ ɢʜᴅ\nʏᴏᴜʀ ᴜsᴇʀ"
                                    ret_ = "sᴜᴄᴄᴇss ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ ᴜsᴇʀ"
                                    ry = str(dhenza.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dhenza.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, " ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ɢʜᴅ\nɴᴀᴍᴇ: ", " \nsᴜᴄᴄᴇss ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ")
                              except:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ")

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            #if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ʀᴇᴊᴇᴄᴛ: {} ɪɴᴠɪᴛᴇᴅ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(msg.to, "ɴᴏᴛʜɪɴɢ ɪɴᴠɪᴛᴇᴅ ɢʀᴏᴜᴘ ʙᴏss")

                        elif cmd == "accept":
                          if wait["selfbot"] == True:
                           # if msg._from in :
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.acceptGroupInvitation(gid)
                                  cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴀᴄᴄᴇᴘᴛ: {} ɪɴᴠɪᴛᴇᴅ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(msg.to, "ɴᴏᴛʜɪɴɢ ɪɴᴠɪᴛᴇᴅ ɢʀᴏᴜᴘ ʙᴏss")
#=========== [ Add Image ] ============#
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ɪᴍᴀɢᴇs...") 
                            else:
                                cl.sendMessage(msg.to, "ɪᴍᴀɢᴇs ɪɴ ʟɪsᴛ") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ ɪᴍᴀɢᴇs {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "ɪᴍᴀɢᴇs ɪs ɴᴏᴛ ʟɪsᴛ") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 ʟɪsᴛ ɢʜᴅ ɪᴍᴀɢᴇ」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nʟɪsᴛ「{}」 ɪᴍᴀɢᴇs".format(str(len(images)))
                             cl.sendMessage(msg.to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.id,msg.to, "ᴘʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴠɪᴅᴇᴏs...") 
                            else:
                                cl.sendMessage(msg.to, "ᴠɪᴅᴇᴏs ɪɴ ʟɪsᴛ") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ ᴠɪᴅᴇᴏs {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "ᴠɪᴅᴇᴏs ɪs ɴᴏᴛ ʟɪsᴛ") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 ʟɪsᴛ ɢʜᴅ ᴠɪᴅᴇᴏ 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nᴛᴏᴛᴀʟ「{}」ᴠɪᴅᴇᴏs".format(str(len(videos)))
                             cl.sendMessage(msg.to, ret_)
                             sendMention1(msg.to, msg._from,"","\nᴊɪᴋᴀ ɪɴɢɪɴ ᴘʟᴀʏ ᴠɪᴅᴇᴏɴʏᴀ,\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ ɴᴀᴍᴀ - ᴊᴜᴅᴜʟ\nʙɪsᴀ ᴊᴜɢᴀ ᴋᴇᴛɪᴋ ɴᴀᴍᴀɴʏᴀ sᴀᴊᴀ ʙᴏss")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ᴍᴘ3 ɴʏᴀ") 
                            else:
                                cl.sendMessage(msg.to, "ᴍᴘ3 ɪᴛᴜ sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ʟɪsᴛ") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ ᴍᴘ3 {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "ᴍᴘ3 ɪᴛᴜ sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ʟɪsᴛ ʙᴏs") 
                                 
                        elif text.lower() == "listmp3":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 ʟɪsᴛ ɢʜᴅ ᴍᴜsɪᴄ 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nᴛᴏᴛᴀʟ「{}」ᴍᴜsɪᴄ".format(str(len(audios)))
                             cl.sendMessage(msg.to, ret_)
                             sendMention1(msg.to, msg._from,"","\nᴊɪᴋᴀ ɪɴɢɪɴ ᴘʟᴀʏ ᴍᴘ3ɴʏᴀ,\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ ɴᴀᴍᴀ - ᴊᴜᴅᴜʟ\nʙɪsᴀ ᴊᴜɢᴀ ᴋᴇᴛɪᴋ ɴᴀᴍᴀɴʏᴀ sᴀᴊᴀ ʙᴏss")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "ᴘʟᴇᴀsᴇ sᴇɴᴅ ɴᴇᴡ sᴛɪᴄᴋᴇʀ...") 
                            else:
                                cl.sendMessage(msg.to, "sᴛɪᴄᴋᴇʀ ɪᴛᴜ ᴅᴀʜ ᴀᴅᴀ ʙᴏs") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ sᴛɪᴄᴋᴇʀ {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                    #       if msg._from in admin:
                             no = 0
                             ret_ = "「 ᴅᴀғᴛᴀʀ sᴛɪᴄᴋᴇʀ」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nᴛᴏᴛᴀʟ「{}」sᴛɪᴄᴋᴇʀ".format(str(len(stickers)))
                             cl.sendMessage(msg.to, ret_)
                             

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ᴏɴ ʙᴏs"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴏɴ ʙᴏs ɪɴ\n ɢʀᴏᴜᴘ: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「ᴅɪᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "ᴡᴇʟʟᴄᴏᴍᴇ ᴍsɢ ᴏғғ ɪɴ\nɢʀᴏᴜᴘ: " +str(ginfo.name)
                                    else:
                                         msgs = "ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ᴏғғ"
                                    cl.sendMessage(msg.to, "「ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ」\n" + msgs)

#===========COMMAND ON OFF============#
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention1(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah slesai, ketik invite off")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention1(msg.to, sender, "", " \nInvite via contact dinonaktifkan")
                               
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 cl.sendMessage(msg.to, "ᴄʜᴇᴄᴋᴘᴏsᴛ ᴏɴ")

                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                cl.sendMessage(msg.to, "ᴄʜᴇᴄᴋᴘᴏsᴛ ᴏғғ")

                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ ʏᴀɴɢ ᴍᴀᴜ ᴅɪ sᴘᴀᴍ ʙᴏs..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                cl.sendMessage(msg.to, "sᴘᴀᴍɪɴᴠɪᴛᴇ sᴜᴅᴀʜ ᴏғғ ʙᴏss")

                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendMention1(msg.to, sender, "「sᴛᴀᴛᴜs ᴜɴsᴇɴᴅ」\nᴜsᴇʀ: ", "\nᴘʟᴇᴀsᴇ ᴜɴsᴇɴᴅ ʏᴏᴜʀ ᴄʜᴀᴛ,\nᴋʟɪᴋ ᴜɴsᴇɴᴅ ᴏɴ ᴀɢᴀɪɴ ɪғ ʏᴏᴜ ᴀᴄᴛɪᴠᴇ ᴜɴsᴇɴᴅ ᴍsɢ")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendMention1(msg.to, sender, "「sᴛᴀᴛᴜs ᴜɴsᴇɴᴅ」\nᴜsᴇʀ ", " \nᴅᴇᴛᴇᴄᴛ ᴜɴsᴇɴᴅ ᴀʟʟ ʀᴇᴀᴅʏ ᴏғғ ʙᴏss")
#===========COMMAND ON OFF============#
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏɴ")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴏғғ")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏғғ")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏ ʀᴇᴀᴅ ᴏғғ")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴏɴ")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴏғғ")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴏɴ")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ ᴏғғ")

                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "   sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nsᴇɴᴅ ʏᴏᴜʀ ᴘᴏsᴛ,\nʟɪᴋᴇ ᴅᴏɴᴇ-> ᴛᴏ ᴏғғ: ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "     sᴛᴀᴛᴜs ᴛɪᴍᴇʟɪɴᴇ ɢʜᴅ\nᴜsᴇʀ: @! \nᴅᴇᴛᴇᴄᴛɪᴏɴ ᴛɪᴍᴇʟɪɴᴇ ᴏғғ")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoBlock"] = True
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀᴅᴅ ᴅɪᴀᴋᴛɪғᴋᴀɴ")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["AutoBlock"] = False
                                cl.sendMessage(msg.to,"ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀᴅᴅ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ")

#===========COMMAND BLACKLIST============#
#===========COMMAND SET============#
                        elif msg.contentType == 16:
                           if wait["Timeline"] == True:
                              msg.contentType = 0
                              msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                              cl.sendMessage(msg.to, "ghd ʟɪᴋᴇ ᴅᴏɴᴇ ʙᴏss")

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʜᴀɴɢᴇ ᴍsɢ")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「ᴍsɢ sᴍs」\nᴍᴇssᴀɢᴇ ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʜᴀɴɢᴇ ᴍsɢ")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ」ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ ᴄʜᴀɴɢᴇ ᴛᴏ\n:\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʜᴀɴɢᴇ ʀᴇsᴘᴏɴ ᴍsɢ")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「ʀᴇsᴘᴏɴ ᴍsɢ」\nʀᴇsᴘᴏɴ ᴍsɢ ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʜᴀɴɢᴇ sᴘᴀᴍ ᴍsɢ")
                              else:
                                  Setmain["message1"] = spl
                                  cl.sendMessage(msg.to, "「sᴘᴀᴍ ᴍsɢ」\nsᴘᴀᴍ ᴍsɢ ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ғᴀɪʟᴇᴅ ᴄʜᴀɴɢᴇ sɪᴅᴇʀ ᴍsɢ")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「sɪᴅᴇʀ ᴍsɢ」\nsɪᴅᴇʀ ᴍsɢ ᴄʜᴀɴɢᴇ ᴛᴏ:\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「ᴄʜᴀᴛ ᴍsɢ」\nᴍʏ ᴍᴇssᴀɢᴇ ᴄʜᴀᴛ:\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「ᴡᴇʟᴄᴏᴍᴇ ᴍsɢ」\nᴍʏ ᴍᴇssᴀɢᴇ ᴡᴇʟᴄᴏᴍᴇ:\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「ʀᴇsᴘᴏɴ ᴍsɢ」\nᴍʏ ᴍᴇssᴀɢᴇ ʀᴇsᴘᴏɴ:\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「sᴘᴀᴍ ᴍsɢ」\nᴍʏ ᴍᴇssᴀɢᴇ sᴘᴀᴍ:\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「sɪᴅᴇʀ ᴍsɢ」\nᴍʏ ᴍᴇssᴀɢᴇ sɪᴅᴇʀ:\n\n「 " + str(wait["mention"]) + " 」")

                        elif ("addfriend " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            cl.findAndAddContactsByMid(str(ls))
                                            cl.sendMessage(msg.to, "Admin Sukses Add Friend "+cl.getContact(str(ls)).displayName)
                                        except:
                                            pass

                        elif cmd.startswith("unfriend "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.deleteContact(ls)
                                cl.sendMessage(msg.to, "Success Unfriend")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendReplyMessage(msg.id,msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
