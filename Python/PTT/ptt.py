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
iLoopIndex = 0


def txtLog(text):
    current_date = time.strftime("%Y_%m_%d")
    current_now = time.strftime("%Y%m%d_%H%M%S")
    txt_url = './' + current_date + '.log'
    f = open(txt_url, "a+")
    f.write(current_now + ' => ' + text + '\n')
    f.close()


def getSoup(_url):
    URL = _url
    my_headers = {'cookie': 'over18=1;'}
    response = requests.get(URL, headers=my_headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup


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
    try:
        url = 'https://www.ptt.cc/bbs/Beauty/index.html'
        key = 'gif'
        print u"search url：" + url
        getPTTLinkByHtml(url)
    except:
        time.sleep(0.1)
    print u"search PTT 結束------"


def getPTTLinkByHtml(_url):
    global aPTTRead
    isFirst = (len(aPTTRead) == 0)
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
                        getPTTStringByHtml(thisText, 'https://www.ptt.cc' + thisUrl)
    if len(aPTTRead) > 30:  # 最多保留30筆
        aPTTRead.remove(aPTTRead[0])


def getPTTStringByHtml(thisText, _url):
    print u'page url：' + _url
    soup = getSoup(_url)
    main_container = soup.find(id='main-container')
    all_a = main_container.find_all('a')
    tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendMessage?"

    for a in all_a:
        contentOne = a.get('href')
        # print contentOne
        if 'gif' in contentOne:
            print str(contentOne)
            txtLog(u"new gif : " + str(contentOne))
            # print("push：" + contentOne)
            tgUrlThis = tgUrl + "chat_id=-1001340182296&parse_mode=HTML&text="
            if thisText != "":
                requests.get(tgUrlThis + thisText, verify=False)
                thisText = ""
            requests.get(tgUrlThis + contentOne, verify=False)
        else:
            print str(contentOne)
            txtLog(u"new img : " + str(contentOne))
            tgUrlThis = tgUrl + "chat_id=-1001253864581&parse_mode=HTML&text="
            if thisText != "":
                requests.get(tgUrlThis + thisText, verify=False)
                thisText = ""
            requests.get(tgUrlThis + contentOne, verify=False)


# PTT End ----------------------------------------------------------------
# HNBang Start ----------------------------------------------------------------
def startHNBang():
    print u"search 很牛幫 開始------"
    try:
        url = 'https://hnbang.com/category/meinv'
        key = 'gif'
        print u"search url：" + url
        getHNBangByHtml(url)
    except:
        time.sleep(0.1)
    print u"search 很牛幫 結束------"


def getHNBangByHtml(_url):
    global aHNBangRead
    isFirst = (len(aHNBangRead) == 0)
    soup = getSoup(_url)
    if not isFirst:
        print u'last new url：' + aHNBangRead[-1]
    for link in soup.find_all('article'):
        if link.find('a'):
            thisUrl = link.find('a').get('href')
            print thisUrl[-10:]
            if thisUrl[-10:] in aHNBangRead:
                time.sleep(0.1)
            else:
                aHNBangRead.append(thisUrl[-10:])
                if not isFirst:
                    print u'new page'
                    txtLog(u"HNBang new page : " + thisUrl)
                    getHNBangStringByHtml(thisUrl)
                    break
    if len(aHNBangRead) > 99:  # 最多保留30筆
        aHNBangRead.remove(aHNBangRead[0])


def getHNBangStringByHtml(_url):
    print u'page url：' + _url
    soup = getSoup(_url)
    article = soup.find('article')
    tgUrl = "https://api.telegram.org/bot1357341611:AAEEazD1g98tQK8W6Q-Qy6Vlu-2VFlrNTa8/sendMessage?"
    tgUrl = tgUrl + "chat_id=-1001340182296&parse_mode=HTML&text="
    for link in article.find_all('img'):
        thisUrl = link.get('src')
        # print thisUrl
        requests.get(tgUrl + thisUrl, verify=False)


# HNBang End ----------------------------------------------------------------
# IG Start ----------------------------------------------------------------
def startIG():
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


def getIGStringByHtml(_url):
    print u'page url：' + _url

    global aIGRead
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
                                try:
                                    if 'display_url' in oEdgesOne['node']:
                                        _files = {
                                            'chat_id': '-1001253864581',
                                            'parse_mode': 'HTML',
                                            'text': oEdgesOne['node']['display_url']
                                        }
                                        txtLog(u"new img")
                                        requests.post(tgUrl, data=_files)
                                except:
                                    time.sleep(0.1)

    aEdges = re['graphql']['user']["edge_felix_video_timeline"]['edges']
    for oEdges in aEdges:
        if oEdges['node']['id'] in aIGRead[_url]:
            time.sleep(0.1)
        else:
            aIGRead[_url].append(oEdges['node']['id'])
            if not isFirst:
                if 'video_url' in oEdges['node']:
                    try:
                        _files = {
                            'chat_id': '-1001340182296',
                            'parse_mode': 'HTML',
                            'text': oEdges['node']['video_url']
                        }
                        txtLog(u"new video")
                        requests.post(tgUrl, data=_files)
                    except:
                        time.sleep(0.1)

    if len(aIGRead[_url]) > 999:  # 最多保留30筆
        aHNBangRead.remove(aIGRead[_url][0])


# IG End ----------------------------------------------------------------

while True:
    print '__________'
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "( " + str(iLoopIndex) + " )"

    # 漫畫 30 * 10 = 300 = 5分鐘
    if iLoopIndex % 30 == 0:
        t_comic = Thread(target=startLoadEpisode)
        t_comic.start()
        time.sleep(0.1)

    # 很牛幫 360 * 10 = 3600 = 1小時
    if iLoopIndex % 360 == 0:
        t1 = Thread(target=startHNBang)
        t1.start()
        time.sleep(0.1)

    # IG 10分鐘
    if iLoopIndex % 60 == 0:
        t_ig = Thread(target=startIG)
        t_ig.start()

    # PTT
    if iLoopIndex >= 0:
        t_ptt = Thread(target=startPTT)
        t_ptt.start()
        t_ptt.join()

    iLoopIndex = iLoopIndex + 1
    for x in range(10):
        print 10 - x
        time.sleep(1)
