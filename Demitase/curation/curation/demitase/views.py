#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2013 NTT MCL Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render_to_response

from curation import commons
from curation import views
from curation.settings import CONSUMER_KEY,CONSUMER_SECRET

import httplib, json
import tweepy
import MeCab
import sys
import string

import urllib
import chardet

from django.utils.html import urlize

import itertools
from operator import itemgetter

from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.pagerank import pagerank
from pygraph.algorithms.demitase_pagerank import demitase_pagerank
from pygraph.classes.exceptions import AdditionError


from readability.readability import Document

userTimeline = []


def extrat_html_document(url):
    html = urllib.urlopen(url).read()
    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

    summary = readable_title.encode('utf-8')
    summary += readable_article.encode('utf-8')
    return summary 

def unique_everseen(iterable, key=None):
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element    

def normalize(tagged):
    return [(item[0].replace('.', ''), item[1]) for item in tagged]


def serve_html(request, page):
    return render_to_response(page+'.html')

def toJSON(objs, status=200):
    json_str = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(json_str, status=status, content_type='application/json; charset=utf-8')

      
def get_timeline(request):
    print "!!!!!"
    global userTimeline
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(request.session.get('key'), request.session.get('secret'))
    api = tweepy.API(auth_handler=auth)
    userTimeline = api.home_timeline(count=500)
    
    return toJSON(len(userTimeline),200)

def timeline(request):

    global userTimeline
    get_no = request.GET.get('query','')
        
    print "GET_NO: " + get_no
    num = 1
    tweet = []
    parsenode = []
    data = []
    ex_url = []

    
    s = userTimeline[int(get_no)]
    tagged = []
    if s.entities.urls:
        for u in s.entities.urls:
      # Facebook, instagram , twitpic 등 사진 url 모두 pass
            print u.expanded_url.encode("utf8")
            if u.expanded_url.encode("utf8").find("fb.me") > 0 or u.expanded_url.encode("utf8").find("instagram") > 0 or u.expanded_url.encode("utf8").find("pic.twitter") > 0:
                print "This link is pic"
                print "mecab_start"
                t = MeCab.Tagger (" ".join(sys.argv))
                m = t.parseToNode(s.text.encode("utf8"))
                continue
                
            print "soup_start"
            try:
                htmlSource = extrat_html_document(u.expanded_url)
                print "soup_end"

#                   Title이 아닌 전체에서 명사 추출
                print "mecab_start"
                t = MeCab.Tagger (" ".join(sys.argv))
                m = t.parseToNode(htmlSource)
            except:
                print "mecab_start"
                t = MeCab.Tagger (" ".join(sys.argv))
                m = t.parseToNode(s.text.encode("utf8"))


#       link 없는 tweet
    else:
        print "mecab_start"
        t = MeCab.Tagger (" ".join(sys.argv))
        m = t.parseToNode(s.text.encode("utf8"))

#       url & text 공통 처리 부분 => mecab
#        temp_surface = "Tweet" + str(num) + " :"
    while m:
        if m.feature.split(",")[0] == "NN":
            try:
                tagged.append((m.surface,m.feature.split(",")[8]))
            except Exception:
                tagged.append((m.surface,"NN"))
        m = m.next


#        tagged = normalize(tagged) # . 제거
    unique_word_set = unique_everseen([x for x in tagged])
    gr = digraph()
    gr.add_nodes(list(unique_word_set))
    
    window_start = 0
    window_end = 2

    while 1:
        window_words = tagged[window_start:window_end]
        if len(window_words) == 2:
#                print window_words
            try:
                gr.add_edge((window_words[0], window_words[1]))   #그래프로  word[0] word[1] 연결
            except AdditionError, e:
                print 'already added %s, %s' % ((window_words[0][0], window_words[1][0]))
        else:
            break
        window_start += 1
        window_end += 1


    calculated_page_rank = demitase_pagerank(gr)     #gr에 있는 keyword 를 pagerank 처리. key 와 graph 처리 값을 이용하여 calculate 하는듯
    di = sorted(calculated_page_rank.iteritems(), key=itemgetter(1))


    key_list = []
    item_num = 0
    temp_surface = "Tweet" + str(num) + " :"
    for k, g in itertools.groupby(reversed(di), key=itemgetter(1)):
        for item in map(itemgetter(0),g):
            temp_surface+= item[0] + " = " + str(k) + " | "
            if item_num < 10:
                key_list.append(item[0])
            else:
                break
            item_num += 1


    parsenode.append(temp_surface)
    print "mecab_end"
    num = num+1
    
    data.append({
        'twt_id':s.id,
        'user_id':s.user.id,
        'username':s.user.name.encode("utf8"),
        'text':urlize(s.text).encode("utf8"),
        'date':str(s.created_at),
        'keywords':key_list,
    })
    # get_no += 1

    return toJSON(data)
    
