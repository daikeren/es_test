# -*- coding: utf-8 -*-

import datetime

from haystack import indexes
from .models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
