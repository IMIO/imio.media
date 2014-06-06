# -*- coding: utf-8 -*-
from zope.interface import implements
from .interfaces import IMediaLink


class MediaLink(object):
    """ """
    implements(IMediaLink)

    def style_attr(self):
        return "width: {};height: {}".format(
            self.maxwidth,
            self.maxheight)
