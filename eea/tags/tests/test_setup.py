""" Tests
"""
import unittest2 as unittest
from Products.CMFCore.utils import getToolByName
from eea.tags.tests.base import EEA_TAGS_POLICY_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):
    """ Test setip
    """
    layer = EEA_TAGS_POLICY_INTEGRATION_TESTING

    def test_css_registry_configured(self):
        """ CSS
        """
        portal = self.layer['portal']
        cssRegistry = getToolByName(portal, 'portal_css')
        self.assertTrue(
            "++resource++eea.tags.css"
            in cssRegistry.getResourceIds()
        )

        # Dependencies
        self.assertTrue(
            "++resource++jquery.tokeninput.css"
            in cssRegistry.getResourceIds()
        )

        self.assertTrue(
            "++resource++jquery.tokeninput.facebook.css"
            in cssRegistry.getResourceIds()
        )

        self.assertTrue(
            "++resource++jquery.tokeninput.mac.css"
            in cssRegistry.getResourceIds()
        )

    def test_css_exists(self):
        """ CSS exists
        """
        portal = self.layer['portal']
        css = portal.restrictedTraverse('++resource++eea.tags.css', None)
        self.assertTrue(css is not None)

        # Dependencies
        css = portal.restrictedTraverse(
            '++resource++jquery.tokeninput.css', None)
        self.assertTrue(css is not None)

        css = portal.restrictedTraverse(
            '++resource++jquery.tokeninput.facebook.css', None)
        self.assertTrue(css is not None)

        css = portal.restrictedTraverse(
            '++resource++jquery.tokeninput.mac.css', None)
        self.assertTrue(css is not None)


    def test_js_registry_configured(self):
        """ JS
        """
        portal = self.layer['portal']
        jsRegistry = getToolByName(portal, 'portal_javascripts')
        self.assertTrue(
            "++resource++eea.tags.js"
            in jsRegistry.getResourceIds()
        )

        self.assertTrue(
            "eea.tags.i18n.js"
            in jsRegistry.getResourceIds())

        # Dependencies
        self.assertTrue(
            "++resource++jquery.tokeninput.js"
            in jsRegistry.getResourceIds()
        )

        self.assertTrue(
            "++resource++jsi18n.js"
            in jsRegistry.getResourceIds()
        )




    def test_js_exists(self):
        """ JS exists
        """
        portal = self.layer['portal']
        js = portal.restrictedTraverse('++resource++eea.tags.js', None)
        self.assertTrue(js is not None)

        js = portal.restrictedTraverse('eea.tags.i18n.js', None)
        self.assertTrue(js is not None)

        # Dependencies
        js = portal.restrictedTraverse('++resource++jquery.tokeninput.js', None)
        self.assertTrue(js is not None)

        js = portal.restrictedTraverse('++resource++jsi18n.js', None)
        self.assertTrue(js is not None)
