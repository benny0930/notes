# -*- coding: utf-8 -*-
import requests
import bs4
import os
import time
from threading import Thread
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
aPTTRead = aHNBangRead = []
aIGRead = {}
aJKFRead = {}
aCKRead = {}
iLoopIndex = 0
iGIFIndex = 0
iIMGIndex = 0


def txtLog(text):
    current_date = time.strftime("%Y_%m_%d")
    current_now = time.strftime("%Y%m%d_%H%M%S")
    txt_url = './' + current_date + '.log'
    f = open(txt_url, "a+")
    f.write(current_now + ' => ' + text + '\n')
    f.close()


def getSoup(_url):
    URL = _url
    # my_headers = {'cookie': 'over18=1;'}
    # response = requests.get(URL, headers=my_headers)
    headers = {'cookie': 'over18=1;',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    response = requests.get(URL, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup


def sendMsg(_type, _text):
    tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendMessage?"
    print _text
    file_path2 = "./NO.txt"
    if not os.path.isfile(file_path2):
        f2 = open(file_path2, 'w')
        f2.close()
    f2 = open(file_path2, 'r')
    file_data = f2.read()
    f2.close()
    aNo = file_data.split(',,,')
    if _text in aNo:
        return 1
    try:
        if 'gif' in _type:
            txtLog(u"new gif : " + _text)
            _files = {
                'chat_id': '-1001340182296',
                'parse_mode': 'HTML',
                'text': _text
            }
        else:
            txtLog(u"new img : " + _text)
            _files = {
                'chat_id': '-1001253864581',
                'parse_mode': 'HTML',
                'text': _text
            }

        requests.post(tgUrl, data=_files)
    except:
        time.sleep(0.1)


def sendImg(_text):
    global iIMGIndex, iGIFIndex

    print _text
    file_path2 = "./NO.txt"
    if not os.path.isfile(file_path2):
        f2 = open(file_path2, 'w')
        f2.close()
    f2 = open(file_path2, 'r')
    file_data = f2.read()
    f2.close()
    aNo = file_data.split(',,,')
    if _text in aNo:
        return 1
    try:
        if 'gif' in _text:
            tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendAudio?"
            txtLog(u"new gif : " + _text)
            _files = {
                'chat_id': '-1001340182296',
                'parse_mode': 'HTML',
                'audio': _text
            }
            iGIFIndex = iGIFIndex + 1
            if iGIFIndex > 100:
                iGIFIndex = 0
                sendMsg('gif',
                        "<p>友站連結：</p><p>正妹圖片群聚地 https://t.me/BeautifulGirlJpg</p><p>正妹GIF群聚地 https://t.me/BeautifulGirlG</p>")
        else:
            tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendPhoto?"
            txtLog(u"new img : " + _text)
            _files = {
                'chat_id': '-1001253864581',
                # 'parse_mode': 'HTML',
                'photo': _text
            }
            iIMGIndex = iIMGIndex + 1
            if iIMGIndex > 100:
                iIMGIndex = 0
                sendMsg('img',
                        "<p>友站連結：</p><p>正妹圖片群聚地 https://t.me/BeautifulGirlJpg</p><p>正妹GIF群聚地 https://t.me/BeautifulGirlG</p>")

        requests.post(tgUrl, data=_files)
    except:
        time.sleep(0.1)


# comic Start ----------------------------------------------------------------
def startLoadEpisode():
    print u"renew comic 開始------"
    txtLog(u"comic start")
    try:

        requests.get('http://benny/api/comic/loadEpisode')
    except:
        time.sleep(0.1)
    print u"renew comic 結束------"
    txtLog(u"comic end")


# comic End ----------------------------------------------------------------
# PTT Start ----------------------------------------------------------------
def startPTT():
    print u"search PTT 開始------"
    txtLog("PTT Start")
    try:
        url = 'https://www.ptt.cc/bbs/Beauty/index.html'
        key = 'gif'
        print u"search url：" + url
        getPTTLinkByHtml(url)
    except:
        time.sleep(0.1)
    print u"search PTT 結束------"
    txtLog("PTT End")


def getPTTLinkByHtml(_url):
    global aPTTRead
    isFirst = (len(aPTTRead) == 0)
    bIMGFirst = True
    bGIFFirst = True
    soup = getSoup(_url)
    if not isFirst:
        print u'new load url：' + aPTTRead[-1]
    for link in soup.find_all('div'):
        if link.get('class') == [u'title']:
            if link.find('a'):
                thisUrl = link.find('a').get('href')
                thisText = link.find('a').text
                try:
                    if u'公告' in thisText:
                        continue
                    elif u'肉特' in thisText:
                        continue
                    elif u'大尺碼' in thisText:
                        continue
                    print(thisText)
                except Exception as e2:
                    thisText = "PTT"
                    print thisUrl

                if thisUrl in aPTTRead:
                    time.sleep(0.1)
                else:
                    aPTTRead.append(thisUrl)
                    if not isFirst:
                        print u'新頁面'
                        txtLog(u"PTT new : " + 'https://www.ptt.cc' + thisUrl)
                        print u'page url：' + 'https://www.ptt.cc' + thisUrl
                        soup = getSoup('https://www.ptt.cc' + thisUrl)
                        main_container = soup.find(id='main-container')
                        all_a = main_container.find_all('a')
                        aSend = []
                        for a in all_a:
                            contentOne = a.get('href')
                            if contentOne[-15:] in aSend:
                                continue
                            else:
                                aSend.append(contentOne[-15:])
                            if 'gif' in contentOne:
                                if bGIFFirst:
                                    bGIFFirst = False
                                    sendMsg('gif', 'https://www.ptt.cc' + thisUrl)
                            else:
                                if bIMGFirst:
                                    bIMGFirst = False
                                    sendMsg('img', 'https://www.ptt.cc' + thisUrl)
                            sendImg(contentOne)
    if len(aPTTRead) > 30:  # 最多保留30筆
        aPTTRead.remove(aPTTRead[0])


# PTT End ----------------------------------------------------------------


# IG Start ----------------------------------------------------------------
def startIG():
    txtLog("IG Start")
    print u"search IG 開始------"
    try:
        file_path1 = "./IG_new.txt"
        if not os.path.isfile(file_path1):
            f1 = open(file_path1, 'w')
            f1.close()

        file_path2 = "./IG.txt"
        if not os.path.isfile(file_path2):
            f2 = open(file_path2, 'w')
            f2.close()

        f1 = open(file_path1, 'r')
        file_data = f1.read()
        f1.close()
        f1 = open(file_path1, 'w')
        f1.close()
        f2 = open(file_path2, 'a+')

        aIGNewUrl = file_data.split(',,,')
        for url in aIGNewUrl:
            if len(url) > 0:
                aIGRead[url] = ['1']
                f2.write(",,," + url)
        f2.close()
        f2 = open(file_path2, 'r')
        file_data = f2.read()
        f2.close()
        aIGUrl = file_data.split(',,,')
        for url in aIGUrl:
            if url != '':
                print u"search url：" + url
                getIGStringByHtml(url)
    except:
        time.sleep(0.1)
    print u"search IG 結束------"
    txtLog("IG End")


def getIGStringByHtml(_url):
    print u'page url：' + _url
    global aIGRead
    bIMGFirst = True
    bGIFFirst = True
    try:
        if _url not in aIGRead:
            aIGRead[_url] = []
        isFirst = (len(aIGRead[_url]) == 0)
        igUrl = "https://www.instagram.com/" + str(_url) + "/?__a=1"
        txtLog(u"igUrl : " + str(igUrl))
        response = requests.get(igUrl)
        re = response.json()
        tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendMessage?"
        aEdges = re['graphql']['user']["edge_owner_to_timeline_media"]['edges']
        for oEdges in aEdges:
            if oEdges['node']['id'] in aIGRead[_url]:
                time.sleep(0.1)
            else:
                aIGRead[_url].append(oEdges['node']['id'])
                if not isFirst:
                    if 'node' in oEdges:
                        if 'edge_sidecar_to_children' in oEdges['node']:
                            if 'edges' in oEdges['node']['edge_sidecar_to_children']:
                                aEdgesOne = oEdges['node']['edge_sidecar_to_children']['edges']
                                for oEdgesOne in aEdgesOne:
                                    if 'display_url' in oEdgesOne['node']:
                                        if bIMGFirst:
                                            bIMGFirst = False
                                            sendMsg('img', igUrl)
                                        sendImg(oEdgesOne['node']['display_url'])
                        elif 'display_url' in oEdges['node']:
                            if bIMGFirst:
                                bIMGFirst = False
                                sendMsg('img', igUrl)
                            sendImg(oEdges['node']['display_url'])

        aEdges = re['graphql']['user']["edge_felix_video_timeline"]['edges']
        for oEdges in aEdges:
            if oEdges['node']['id'] in aIGRead[_url]:
                time.sleep(0.1)
            else:
                aIGRead[_url].append(oEdges['node']['id'])
                if not isFirst:
                    if 'video_url' in oEdges['node']:
                        if bGIFFirst:
                            bGIFFirst = False
                            sendMsg('gif', igUrl)
                        sendMsg('gif', oEdges['node']['video_url'])

        if len(aIGRead[_url]) > 999:  # 最多保留30筆
            aHNBangRead.remove(aIGRead[_url][0])
    except Exception as e2:
        print e2


# IG End ----------------------------------------------------------------
# JKF Start ----------------------------------------------------------------
def startJKF():
    txtLog("JKF Start")
    print u"search JKF 開始------"
    try:
        # aId = ['393', '520', '1112', '574', '640', '611', '587', '535', '234']
        file_path2 = "./JKF.txt"
        if not os.path.isfile(file_path2):
            f2 = open(file_path2, 'w')
            f2.close()
        f2 = open(file_path2, 'r')
        file_data = f2.read()
        f2.close()
        aId = file_data.split(',,,')

        for sId in aId:
            print u"search sId：" + str(sId)
            getJKFLinkByHtml(sId)
    except:
        print u"search JKF 錯誤------"
    print u"search JKF 結束------"
    txtLog("JKF End")


def getJKFLinkByHtml(_id):
    global aJKFRead
    try:
        if _id not in aJKFRead:
            aJKFRead[_id] = []
        url = 'https://www.jkforum.net/forum.php?mod=forumdisplay&typeid=&fid=' + str(
            _id) + '&orderby=dateline&filter=dateline&dateline=86400&typeid=&orderby=dateline'
        print url
        isFirst = (len(aJKFRead[_id]) == 0)
        soup = getSoup(url)
        if not isFirst:
            print u'new load _id：' + _id
        waterfall = soup.find(id="waterfall")
        test = waterfall.find_all('li')
        for link in waterfall.find_all('li'):
            if link.find('a'):
                thisUrl = link.find('a').get('href')
                aThisUrl = thisUrl.split('&')
                print thisUrl
                if aThisUrl[1] in aJKFRead[_id]:
                    time.sleep(0.1)
                else:
                    aJKFRead[_id].append(aThisUrl[1])
                    if not isFirst:
                        print u'新頁面'
                        txtLog(u"JKF new : " + 'https://www.JKF.cc' + thisUrl)
                        getJKFStringByHtml('https://www.jkforum.net/' + thisUrl)
        if len(aJKFRead) > 999:  # 最多保留30筆
            aJKFRead.remove(aJKFRead[0])
    except Exception as e2:
        print e2
        print u"getJKFLinkByHtml JKF 錯誤------"


def getJKFStringByHtml(_url):
    print u'page url：' + _url
    bIMGFirst = True
    bGIFFirst = True
    soup = getSoup(_url)
    ignore_js_op = soup.find_all('ignore_js_op')
    aSend = []
    # if len(ignore_js_op) > 0:
    #     sendImg(_url)
    for op in ignore_js_op:
        img = op.find('img')
        contentOne = img.get('file')
        if contentOne in aSend:
            continue
        else:
            aSend.append(contentOne)
        # print contentOne
        if 'gif' in contentOne:
            if bGIFFirst:
                bGIFFirst = False
                sendMsg('gif', _url)
        else:
            if bIMGFirst:
                bIMGFirst = False
                sendMsg('img', _url)
        sendImg(contentOne)


# JKF End ----------------------------------------------------------------

# CK Start ----------------------------------------------------------------
def startCK():
    txtLog("CK Start")
    print u"search CK 開始------"
    try:
        # aId = ['forum-3866-1']
        file_path2 = "./CK.txt"
        if not os.path.isfile(file_path2):
            f2 = open(file_path2, 'w')
            f2.close()
        f2 = open(file_path2, 'r')
        file_data = f2.read()
        f2.close()
        aId = file_data.split(',,,')

        for sId in aId:
            print u"search sId：" + str(sId)
            getCKLinkByHtml(sId)
    except:
        print u"search CK 錯誤------"
    print u"search CK 結束------"
    txtLog("CK End")


def getCKLinkByHtml(_id):
    global aCKRead
    try:
        if _id not in aCKRead:
            aCKRead[_id] = []
        url = 'https://ck101.com/' + str(_id) + '.html?order_by=dateline'

        isFirst = (len(aCKRead[_id]) == 0)
        soup = getSoup(url)
        if not isFirst:
            print u'new load _id：' + _id
        table = soup.find(id="threadlisttableid")
        for tbody in table.find_all('tbody'):
            tid = str(tbody.get('tid'))
            if tid != 'None':
                if tid in aCKRead[_id]:
                    time.sleep(0.1)
                else:
                    aCKRead[_id].append(tid)
                    thisUrl = 'https://ck101.com/thread-' + tid + '-1-1.html'
                    print thisUrl
                    if not isFirst:
                        print u'新頁面'
                        txtLog(u"CK new : " + thisUrl)
                        getCKStringByHtml(thisUrl)
        if len(aCKRead) > 999:  # 最多保留30筆
            aCKRead.remove(aCKRead[0])
    except Exception as e2:
        print e2
        print u"getCKLinkByHtml CK 錯誤------"


def getCKStringByHtml(_url):
    print u'page url：' + _url
    soup = getSoup(_url)
    table = soup.find(id="lightboxwrap")
    imgs = table.find_all('img')
    aSend = []
    bIMGFirst = True
    bGIFFirst = True
    # if len(imgs) > 0:
    #     sendImg(_url)
    for img in imgs:
        contentOne = img.get('file')
        if contentOne:
            aContentOne = contentOne.split('?')
            contentOne = aContentOne[0]
            if contentOne in aSend:
                continue
            else:
                aSend.append(contentOne)
            if 'gif' in contentOne:
                if bGIFFirst:
                    bGIFFirst = False
                    sendMsg('gif', _url)
            else:
                if bIMGFirst:
                    bIMGFirst = False
                    sendMsg('img', _url)
            sendImg(contentOne)


# CK End ----------------------------------------------------------------
while True:
    print '__________'
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "( " + str(iLoopIndex) + " )"

    # PTT
    if iLoopIndex >= 0:
        t_ptt = Thread(target=startPTT)
        t_ptt.start()
        t_ptt.join()

    # 漫畫 5分鐘
    if iLoopIndex % 30 == 0:
        t_comic = Thread(target=startLoadEpisode)
        t_comic.start()
        time.sleep(0.1)

    # IG 10分鐘
    if iLoopIndex % 60 == 0:
        t_ig = Thread(target=startIG)
        t_ig.start()

    # JKF 12分鐘
    if iLoopIndex % 72 == 0:
        t_ptt = Thread(target=startJKF)
        t_ptt.start()
        t_ptt.join()

    # CK 14分鐘
    if iLoopIndex % 84 == 0:
        t_ptt = Thread(target=startCK)
        t_ptt.start()
        t_ptt.join()

    iLoopIndex = iLoopIndex + 1
    for x in range(10):
        print 10 - x
        time.sleep(1)
