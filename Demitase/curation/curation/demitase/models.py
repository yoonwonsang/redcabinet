# -*- coding: utf-8 -*-

from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=128)
    email = models.EmailField(null=True)
    user_twt_id = models.CharField(max_length = 128, null=True)

class HomeTimelineTmp(models.Model):
    user_id = models.CharField(max_length = 32)
    content_type = models.CharField(max_length = 32)
    content_seq = models.IntegerField()
    content_id = models.CharField(max_length = 32)
    content_autr_id = models.CharField(max_length = 128, null = True)
    content_autr_nm = models.CharField(max_length = 128, null = True)
    content_autr_img = models.CharField(max_length = 256, null = True)
    text = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add = False, null = True)
    url_cnt = models.IntegerField(null=True)
    
class HomeTimelineUrlTmp(models.Model):
    user_id = models.CharField(max_length = 32)
    twt_id = models.CharField(max_length = 32)
    url_seq = models.IntegerField()
    url = models.CharField(max_length = 256)
    expanded_url = models.CharField(max_length = 256)
    
class Keywords(models.Model):
#     keyword_id = models.IntegerField()
    keyword_name = models.CharField(max_length = 128)
    
# class ContentSource(models.Model):
#     content_type = models.CharField(max_length = 32)
#     content_src_name = models.CharField(max_length = 128)
    
class ContentKeywords(models.Model):
    content_type = models.CharField(max_length = 128)
    content_id = models.CharField(max_length = 32)
    keyword_seq = models.IntegerField()
    keyword_id = models.IntegerField()
    
class ContentDetail(models.Model):
    content_type = models.CharField(max_length = 32)
    content_id = models.CharField(max_length = 128)
    content_text = models.TextField()
    content_autr_id = models.CharField(max_length = 128)
    content_autr_nm = models.CharField(max_length = 128)
    content_autr_img = models.CharField(max_length = 256)
    content_created_at = models.DateTimeField(auto_now_add = False)
    content_key_cnt = models.IntegerField()
    
class UserInfoStream(models.Model):
    user_id = models.CharField(max_length = 32)
    content_type = models.CharField(max_length = 32)
    content_id = models.CharField(max_length = 32)
    
