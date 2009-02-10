from pastgit.lib.paste import *

from subprocess import Popen, PIPE

from uuid import uuid4

class PasterDao(object):
    def create(self, initial):
        paste = Paste("data/pastes", uuid4())
        paste.create(initial)
        return paste

    def get(self, id):
        return Paste("data/pastes", id)

    def list(self):
        ls = Popen("ls data/pastes/*.git/modified --sort=time", shell=True, stdout=PIPE)
        return [x[len('data/pastes/'):(len(x)-len('.git/modified'))] for x in ls.communicate()[0].split('\n') if x]
