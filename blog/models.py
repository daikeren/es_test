# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


class Blog(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=1024)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.pk, ])
