# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFPlone.utils import get_installer
from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from collective.workcalendar import testing  # noqa: E501

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.workcalendar is properly installed."""

    layer = testing.COLLECTIVE_WORKCALENDAR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.workcalendar is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.workcalendar"))

    def test_browserlayer(self):
        """Test that ICollectiveWorkcalendarLayer is registered."""
        from collective.workcalendar.interfaces import ICollectiveWorkcalendarLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveWorkcalendarLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = testing.COLLECTIVE_WORKCALENDAR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.workcalendar")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.workcalendar is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.workcalendar"))

    def test_browserlayer_removed(self):
        """Test that ICollectiveWorkcalendarLayer is removed."""
        from collective.workcalendar.interfaces import ICollectiveWorkcalendarLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveWorkcalendarLayer, utils.registered_layers())
