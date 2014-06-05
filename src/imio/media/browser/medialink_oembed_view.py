# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from collective.oembed import consumer


class MediaLinkView(BrowserView):
    """Aggregate all services in the following order:
      * oembed
      * api2embed
      * url2embed
    """

    def embed(self):
        consumer_view = consumer.ConsumerView(self.context, self.request)
        if not consumer_view:
            return u""

        consumer_view._url = self.context.remoteUrl
        return consumer_view.get_embed_auto()

    def get_style(self):
        result = ''
        if self.context.maxwidth:
            result += 'max-width: {}px;'.format(self.context.maxwidth)

        if self.context.maxheight:
            result += 'max-height: {}px;'.format(self.context.maxheight)

        return result
