# -*- coding: utf-8 -*-
from collective.oembed.consumer import ConsumerView

from collective.oembed import endpoints
from collective.oembed.api2embed import structure as api2embed_structure
from collective.oembed.url2embed import structure as url2embed_structure
from imio.media.endpoints import get_structure


class MedialinkConsumerView(ConsumerView):
    def __init__(self, context, request):
        super(MedialinkConsumerView, self).__init__(context, request)

    def update(self):
        if not self.structure:
            s_cookieless = get_structure()
            s_endpoints = endpoints.get_structure()
            s_url2embed = url2embed_structure.get_structure()
            s_api2embed = api2embed_structure.get_structure()
            for providers in (s_cookieless, s_endpoints, s_url2embed, s_api2embed):
                for hostname in providers:
                    if hostname not in self.structure:
                        self.structure[hostname] = []
                    infos = providers[hostname]
                    for info in infos:
                        self.structure[hostname].append(info)
