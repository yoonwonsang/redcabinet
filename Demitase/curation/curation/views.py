from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.generic import View
from  django.core.urlresolvers import reverse
import httplib, json
from curation import commons
from curation.settings import CONSUMER_KEY,CONSUMER_SECRET,CALLBACK_URL
from urllib import *
from urllib2 import *
import tweepy
import re


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET,CALLBACK_URL)
verifier = ''
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


def index(request):
	return HttpResponseRedirect('/login/')

def logout(request):
    try:
        del request.session['key']
        return HttpResponseRedirect('/login/')
    except:
        return HttpResponseRedirect('/login/')


'''
def login(request):
    if commons.logged_in(request):
        HttpResponseRedirect('/home/demitase.html')
#        return main(request)

    if 'username_or_email' in request.POST and 'password' in request.POST: 
        (username, password) = (request.POST['username_or_email'], request.POST['password'])
        aurl = auth.get_authorization_url()
        request_token = auth.request_token
        # print "AURL: " + aurl
        # print "RTOKEN: " + request_token
        
        return HttpResponseRedirect(aurl)
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
                    valued["session[username_or_email]"] = username
                elif '"password"' in inputd:
                    valued["session[password]"] = password
                elif inputd.get("type",0) == "submit":
                    valued["submit"] = inputd["value"]
                else:
                    print inputd
            else:
                break

        params = urlencode(valued)
        req = Request(actionURL, params)
        res = urlopen(req)
        data = res.read()
        lines = data.splitlines()
        tokens = []
        for index, line in enumerate(lines):
            if "code-desc" in line and "code" in line:
                index += 1
                break
        verifier = lines[index].lstrip('<kbd aria-labelledby="code-desc"><code>').rstrip('</code></kbd>')
        print verifier
        print auth
        auth.get_access_token(verifier)
       # header = {'Content-type': 'application/json'}
       # body = {'auth': {'passwordCredentials': {'username_or_email': username, 'password': password}}}

        # TODO: Error Handling
        #data = json.loads(response.read())
        #conn.close()
        #request.session['access'] = data['access']
        #request.session['access'] = 'temppassauth'  #need to recover
        request.session['access'] = request.POST['username_or_email']
	print request.POST['username_or_email']
        print "before main"
        #main(request,auth)
        return HttpResponseRedirect('/home/demitase.html')
    else:
#        t = loader.get_template('tweet.html')
        t = loader.get_template('tweet.html')

        c = {}
        c.update(csrf(request))
        c = Context(c)

        return HttpResponse(t.render(c))
'''

#def main(request):
#    print "main function"
#    num = 1
#    api = tweepy.API(auth)
#    print auth
#    for s in api.home_timeline(count=50):
#	print "Tweet"+ str(num) + " :"+s.text.encode("utf8")
#	num = num+1


def login(request):
    return render_to_response('oauth/index.html')
 
def Get(request):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)
    try :
        auth_url = auth.get_authorization_url(True)
    except tweepy.TweepError:
        print 'Error! Failed to get request token'
 
    request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)
    return HttpResponseRedirect(auth_url)
 
 
def get_callback(request):
    '''
    Callback
    '''
    # Example using callback (web app)
    verifier = request.GET.get('oauth_verifier')
    print verifier

    # Let's say this is a web app, so we need to re-build the auth handler first...
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    

    token = request.session.get('request_token')
    del request.session['request_token']
    auth.set_request_token(token[0], token[1])
    
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    request.session['key'] = auth.access_token.key
    request.session['secret'] = auth.access_token.secret
    request.session.set_expiry(600)
     
    return HttpResponseRedirect('/home/demitase.html')
