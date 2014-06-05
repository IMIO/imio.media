# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from plone.supermodel import model
from zope.schema import TextLine, Int
from . import _


class IImioMediaLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IMediaLink(model.Schema):
    """ Schema for MediaLink template """
    remoteUrl = TextLine(
        title=_(u'URL'),
        description=u'',
        default=u'http://'
    )

    maxwidth = Int(
        title=_(u'Max width'),
        description=_(u'Like "1024", this value is in pixel'),
        required=False,
        default=1024,
    )

    maxheight = Int(
        title=_(u'Max height'),
        description=_(u'Like "768", this value is in pixel'),
        required=False,
    )
