# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView


class MediaLinkView(BrowserView):
    """Aggregate all services in the following order:
      * oembed
      * api2embed
      * url2embed
    """

    def embed(self):
        oembed = self.context.restrictedTraverse('@@proxy-oembed-provider')
        if oembed is None:
            return u""
        return oembed.get_embed(self.context.remoteUrl)

    def get_style(self):
        return "max-width: {}px;max-height: {}px".format(
            self.context.maxwidth,
            self.context.maxheight)
