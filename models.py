#!/usr/bin/env python3

''' Define Posts and Comments so that each post can contain a comment'''

import datetime
from flask import url_for
from tumblelog import database


class Comment(database.EmbeddedDocument):
    
    """The comment model comes first because it's called in the Post one. Defines the 'Comment' model (author, body), sustain by the index created_at"""
    
    created_at = database.DateTimeField(default=datetime.datetime.now, required=True)
    body = database.StringField(verbose_name="Comment", required=True)
    author = database.StringField(verbose_name="Name", max_length=255, required=True)
    

class Post(database.Document):
    
    """This model defines the 'Post' model (title, slug, body) sustain by the index created_at"""
    
    created_at = database.DateTimeField(default=datetime.datetime.now, required=True)
    title = database.StringField(max_length=255, required=True)
    slug = database.StringField(max_length=255, required=True)
    body = database.StringField(required=True)
    comments = database.ListField(database.EmbeddedDocumentField("Comment"))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
    
     
    