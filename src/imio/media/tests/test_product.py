# -*- coding: utf-8 -*-
import unittest2 as unittest
from zope.event import notify
from zope.traversing.interfaces import BeforeTraverseEvent
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone import api
from imio.media.testing import IMIO_MEDIA_INTEGRATION
from lxml import html

class TestIntegration(unittest.TestCase):
    layer = IMIO_MEDIA_INTEGRATION

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.request['ACTUAL_URL'] = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        notify(BeforeTraverseEvent(self.portal, self.request))

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        pid = 'imio.media'
        installed = [p['id'] for p in qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_view(self):
        # Get the vienk_oembed_viewOw
        multimedia = api.content.create(
            container=self.portal,
            type='media_link',
            title='video',
            remoteUrl='http://vimeo.com/95988841')
        self.failUnless(multimedia.view())
