import logging

from pastgit.lib.base import *
from pylons.decorators import rest

from formencode import variabledecode

log = logging.getLogger(__name__)

class DashboardController(BaseController):

    @rest.dispatch_on(POST='_postPaste')
    def index(self):
        return render("newpaste")

    def _postPaste(self):
        post = variabledecode.variable_decode(request.POST)
        log.info("post: " + str(post))

        if not post.get("fileContent"):
            return "empty"

        return "pasted"
