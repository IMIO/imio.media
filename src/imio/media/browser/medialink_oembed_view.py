# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from imio.media.browser import utils


class MediaLinkView(BrowserView):
    """Aggregate all services in the following order:
      * oembed
      * api2embed
      * url2embed
    """

    def description(self):
        return self.context.description

    def rich_description(self):
        return self.context.richdescription.output if self.context.richdescription is not None else ''

    def embed(self):
        return utils.embed(self.context, self.request)

    def get_style(self):
        return utils.get_style(self.context)
