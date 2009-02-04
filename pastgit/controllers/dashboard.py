import logging

from pastgit.lib.base import *

log = logging.getLogger(__name__)

class DashboardController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        return render("dashboard")
