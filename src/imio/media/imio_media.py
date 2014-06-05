# -*- coding: utf-8 -*-
from plone.app.contenttypes.content import Link
from zope.interface import implements
from .interfaces import IMediaLink


class MediaLink(Link):
    """ """
    implements(IMediaLink)

    def style_attr(self):
        return "width: {};height: {}".format(
            self.maxwidth,
            self.maxheight)
