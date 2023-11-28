# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.workcalendar


class CollectiveWorkcalendarLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.

        self.loadZCML(package=collective.workcalendar)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.workcalendar:default")


COLLECTIVE_WORKCALENDAR_FIXTURE = CollectiveWorkcalendarLayer()


COLLECTIVE_WORKCALENDAR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_WORKCALENDAR_FIXTURE,),
    name="CollectiveWorkcalendarLayer:IntegrationTesting",
)


COLLECTIVE_WORKCALENDAR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_WORKCALENDAR_FIXTURE,),
    name="CollectiveWorkcalendarLayer:FunctionalTesting",
)


COLLECTIVE_WORKCALENDAR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_WORKCALENDAR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveWorkcalendarLayer:AcceptanceTesting",
)
