# -*- coding: utf-8 -*-

from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    user_twt_id = models.CharField(max_length = 128, blank=True)

class HomeTimelineTmp(models.Model):
    user_id = models.CharField(max_length = 32)
    seq = models.IntegerField()
    twt_id = models.CharField(max_length = 32)
    twt_author_id = models.CharField(max_length = 128)
    twt_author_nm = models.CharField(max_length = 128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = False)
    url_cnt = models.IntegerField()
    
class HomeTimelineUrlTmp(models.Model):
    user_id = models.CharField(max_length = 32)
    twt_id = models.CharField(max_length = 32)
    url_seq = models.IntegerField()
    url = models.CharField(max_length = 256)
    expanded_url = models.CharField(max_length = 256)
    
class Keywords(models.Model):
    keyword_id = models.CharField(max_length = 32)
    keyword_name = models.CharField(max_length = 128)
    
class ContentSource(models.Model):
    content_type = models.CharField(max_length = 32)
    content_src_name = models.CharField(max_length = 128)
    
class ContentKeywords(models.Model):
    content_type = models.OneToOneField(ContentSource)
    content_id = models.CharField(max_length = 128)
    keyword_id = models.OneToOneField(Keywords)
    
#class UserInfoStream(models.Model):
#    user_id = models.OneToOneField(User)
#    content_type = models.ForeignKey('ContentKeywords')
#    content_id = models.ForeignKey('ContentKeywords')
    