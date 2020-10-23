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