import logging

from pastgit.lib.base import *
from pastgit.lib.pasterdao import *
from pylons.decorators import rest

from formencode import variabledecode
from pastgit.lib.relativetime import *

log = logging.getLogger(__name__)

class DashboardController(BaseController):

    def __init__(self):
        self.paster = PasterDao()

    @rest.dispatch_on(POST='_postPaste')
    def index(self):
        c.fileId = 1
        return render("newpaste")

    def pasteBox(self, id = None):
        if id == None:
            c.fileId = 1
        else:
            c.fileId = id
        return render("pasteBox")

    def _postPaste(self):
        post = variabledecode.variable_decode(request.POST)
        log.info("post: " + str(post))

        if not post.get("fileContent"):
            return "empty"

        initial = zip(xrange(10000),post.get("fileName"), post.get("fileContent"))
        log.info(initial)

        paste = self.paster.create(initial)
        c.pasteId = paste.id

        return render("pasted")

    def show(self, id, rev=None):
        c.pasteId = id
        paste = self.paster.get(id)
        c.blobs = paste.show()

        c.history = [(x.id[0:5], x.id, relative_time(x.committed_date)) for x in paste.history()]
        return render("showPaste")

    @rest.dispatch_on(POST='_savePaste')
    def edit(self, id):
        c.pasteId = id
        paste = self.paster.get(id)
        c.blobs = paste.show()
        return render("editPaste")

    def _savePaste(self, id):
        post = variabledecode.variable_decode(request.POST)

        content = zip(post.get("fileName"), post.get("fileContent"))

        paste = self.paster.get(id)
        paste.modify(content)

        redirect_to(controller="/dashboard", id=id, action="show", rev=None)
