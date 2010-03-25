import logging

from pastgit.lib.base import *
from pastgit.lib.pasterdao import *
from pylons.decorators import rest

from itertools import count
from formencode import variabledecode
from pastgit.lib.relativetime import *

from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename, guess_lexer
from pygments.formatters import HtmlFormatter

log = logging.getLogger(__name__)

class HighlightedBlob(object):
    pass

class DashboardController(BaseController):

    languages = dict(txt = "Plain Text",
                     java = "Java",
                     js = "JavaScript",
                     css = "CSS",
                     xml = "XML")

    def __init__(self):
        self.paster = PasterDao()

    @rest.dispatch_on(POST='_postPaste')
    def index(self):
        self._prepareLanguages()
        return render("newpaste")

    def pasteBox(self, id = None):
        self._prepareLanguages()
        return render("pasteBox")

    def _postPaste(self):
        content = self._contentFromPost(request.POST)

        paste = self.paster.create(content)
        c.pasteId = paste.id

        return render("pasted")

    def raw(self, id, rev=None, file=None):
        c.pasteId = id

        paste = self.paster.get(id)
        c.blobs = paste.show(rev)

        response.headers['content-type'] = 'text/xml; charset=utf-8'

        return str([x.data for x in c.blobs if x.name == file][0])

    def show(self, id, rev=None):
        c.pasteId = id

        paste = self.paster.get(id)
        c.blobs = paste.show(rev)

        c.blobs = [self._highlightBlob(x) for x in c.blobs]

        history = paste.history()
        
        c.currentRev = history[0].id
        if rev:
            c.currentRev = rev

        c.history = [(x.id[0:5], x.id, relative_time(x.committed_date), c.currentRev == x.id and "current" or "other") for x in history]

        c.editable =  c.currentRev == history[0].id

        c.highlighterStyles = HtmlFormatter().get_style_defs('.fileContent')

        return render("showPaste")

    @rest.dispatch_on(POST='_savePaste')
    def edit(self, id):
        c.pasteId = id
        self._prepareLanguages()

        paste = self.paster.get(id)
        c.blobs = paste.show()
        return render("editPaste")

    def _savePaste(self, id):
        content = self._contentFromPost(request.POST)

        paste = self.paster.get(id)
        paste.modify(content)

        redirect_to(controller="/dashboard", id=id, action="show", rev=None)

    def _contentFromPost(self, requestPost):
        post = request.POST 

        res = zip(count(), post.getall("fileName"), post.getall("fileContent"), post.getall("language"))

        log.info("content from post" + str(res))
        return res

    def _prepareLanguages(self):
        c.languages = self.languages.items()

    def _highlightBlob(self, blob):
        res = HighlightedBlob()

        res.id = blob.id
        res.name = blob.name
        res.data = blob.data

        try:
            lexer = guess_lexer_for_filename(blob.name, blob.data)
        except:
            try:
                lexer = guess_lexer(blob.data)
            except:
                lexer = get_lexer_by_name("text")

        formatter = HtmlFormatter(cssclass="source")
        result = highlight(blob.data, lexer, formatter)

        res.data = result

        return res

    def list(self):
        c.ids = self.paster.list()
        return render('list')
