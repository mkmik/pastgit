from pastgit.lib.paste import *

from uuid import uuid4

class PasterDao(object):
    def create(self, initial):
        paste = Paste("data/pastes", uuid4())
        paste.create(initial)
        return paste

    def get(self, id):
        return Paste("data/pastes", id)
