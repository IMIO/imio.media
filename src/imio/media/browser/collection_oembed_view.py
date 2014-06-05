# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from collective.oembed import consumer


class CollectionOembedView(BrowserView):
    """Aggregate all services in the following order:
      * oembed
      * api2embed
      * url2embed
    """

    def embed(self, obj):
        consumer_view = consumer.ConsumerView(obj, self.request)
        if not consumer_view:
            return u""
        consumer_view._url = obj.remoteUrl

        return consumer_view.get_embed_auto()

    def get_style(self, obj):
        result = ''
        if obj.maxwidth:
            result += 'max-width: {}px;'.format(obj.maxwidth)

        if obj.maxheight:
            result += 'max-height: {}px;'.format(obj.maxheight)

        return result
