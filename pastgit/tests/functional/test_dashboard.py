from pastgit.tests import *

class TestDashboardController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='dashboard'))
        # Test response...
