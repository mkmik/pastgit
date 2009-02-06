import logging

import os, shutil
from git import *

log = logging.getLogger(__name__)

class Paste(object):
    def __init__(self, base, id):
        self.base = base
        self.id = id
        self.dirname = base + "/" + str(id) + ".git"
        self.wcname = self.dirname + "-wc"

    def create(self, content):
        self.repo = Repo.create(self.dirname)
        
        os.mkdir(self.wcname)
        git = Git(self.wcname)
        git.init()

        for pos, name, body in content:
            fname = name
            if not fname:
                fname = "pastefile" + str(pos)
            f = open(self.wcname + "/" + fname, "w")
            print >>f, body
            f.close()

        git.add(".")
        git.commit(message="initial")
        git.push("--all", repo="../../../" + self.dirname)

        shutil.rmtree(self.wcname)

    def show(self):
        self.repo = Repo(self.dirname)
        return [x for x in self.repo.tree().contents if x.name != ".gitignore"]

    def history(self):
        self.repo = Repo(self.dirname)
        return self.repo.commits()

    def modify(self, content):
        log.info("todo: modify" + str(content))

        rep = Git(self.dirname)
        rep.clone(".", "../../../" + self.wcname)
        git = Git(self.wcname)

        for fname, body in content:
            f = open(self.wcname + "/" + fname, "w")
            print >>f, body
            f.close()

        git.add(".")
        git.commit(message="web edit")
        git.push("--all", repo="../../../" + self.dirname)

        shutil.rmtree(self.wcname)
