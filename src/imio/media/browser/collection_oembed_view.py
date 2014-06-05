# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView


class CollectionOembedView(BrowserView):
    """Aggregate all services in the following order:
      * oembed
      * api2embed
      * url2embed
    """

    def embed(self, obj):
        oembed = obj.restrictedTraverse('@@proxy-oembed-provider')
        if oembed is None:
            return u""
        return oembed.get_embed(obj.remoteUrl)

    def get_style(self, obj):
        return "max-width: {}px;max-height: {}px".format(
            obj.maxwidth,
            obj.maxheight)
