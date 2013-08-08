#!/usr/bin/python
#-*- coding:utf-8 -*-

USERNAME = "sungjin7@gmail.com"
PASSWORD = "elfpr*^tjdwls!"

import tweepy

import re

roToken = re.compile("<\w+|>|/>|</\w+>|\w+|=|\"[^\"]+\"")

def GetTagAttrd(tokens, beginTag, endTag, curIndex, endIndex):
    itokens = []
    try:
        curIndex = tokens.index(beginTag, curIndex)
    except ValueError:
        return curIndex, None

    if curIndex >= endIndex:
        return endIndex, None

    while tokens[curIndex] != endTag:
            itokens.append(tokens[curIndex])
            curIndex += 1

    return curIndex, dict(zip(itokens[1::3], [val[1:-1] for val in itokens[3::3]]))


from urllib import *
from urllib2 import *

def printout(auth):
    print "printout"
    api = tweepy.API(auth)

    for s in api.home_timeline(count=1):
        print s.text.encode("utf8")


def Main():
    CONSUMER_KEY = 'QN5inGo2xmA7717qxCQ'
    CONSUMER_SECRET = 'dxOvz4PmcWBrQlEkFpK9lu68dT1q0QNEB4UVMYWpmRI'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    aurl = auth.get_authorization_url()
    data = urlopen(aurl).read()
    lines = data.splitlines()
    tokens = []
    for line in lines:
        tokens += roToken.findall(line)

    curIndex, formd = GetTagAttrd(tokens, '<form', '>', 0, len(tokens))
    endIndex = tokens.index('</form>', curIndex)
    actionURL = formd["action"]


    valued = {}
    while True:
        curIndex, inputd = GetTagAttrd(tokens, "<input", "/>", curIndex, endIndex)
        if inputd:
            if "type" in inputd:
                valued[inputd["name"]] = inputd["value"]
            elif '"text"' in inputd:
                valued["session[username_or_email]"] = USERNAME
            elif '"password"' in inputd:
                valued["session[password]"] = PASSWORD
            elif inputd.get("type",0) == "submit":
                valued["submit"] = inputd["value"]
            else:
                print inputd
        else:
            break

    #print valued
    params = urlencode(valued)
   # print params
    #print actionURL
    req = Request(actionURL, params)
   # print req
    res = urlopen(req)
    data = res.read()
    lines = data.splitlines()
    tokens = []
    for index, line in enumerate(lines):
        if "code-desc" in line and "code" in line:
            index += 1
            break
#    verifier = lines[index].strip()
    verifier = lines[index].lstrip('<kbd aria-labelledby="code-desc"><code>').rstrip('</code></kbd>')
    print "sungjin"
    print verifier
    auth.get_access_token(verifier)

    printout(auth)
#    if 0:
#        api.update_status(u"~tweepy test")
#    else:
#        for s in api.user_timeline():
#            print s.text.encode("utf8")

Main()

