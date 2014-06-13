# -*- coding: utf-8 -*-
from collective.oembed import consumer


def embed(media, request):
    consumer_view = consumer.ConsumerView(media, request)
    if not consumer_view or not getattr(media, 'remoteUrl', False):
        return u""
    consumer_view._url = media.remoteUrl

    return consumer_view.get_embed_auto()


def get_style(media):
    result = ''
    if media.maxwidth:
        result += 'max-width: {}px;'.format(media.maxwidth)

    if media.maxheight:
        result += 'max-height: {}px;'.format(media.maxheight)

    return result
