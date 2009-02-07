import logging

import os, os.path, shutil
from git import *

log = logging.getLogger(__name__)

class Paste(object):
    def __init__(self, base, id):
        self.base = base
        self.id = id
        self.dirname = os.path.abspath(base + "/" + str(id) + ".git")
        self.wcname = self.dirname + "-wc"

    def create(self, content):
        self.repo = Repo.create(self.dirname)
        
        os.mkdir(self.wcname)
        git = Git(self.wcname)
        git.init()

        self.writeContent(content)

        git.add(".")
        git.commit(message="initial")
        git.push("--all", repo=self.dirname)

        shutil.rmtree(self.wcname)

    def show(self, rev=None):
        if not rev:
            rev = "master"
        self.repo = Repo(self.dirname)
        return self.repo.tree(rev).values()

    def history(self):
        self.repo = Repo(self.dirname)
        return self.repo.commits()

    def modify(self, content):
        log.info("todo: modify" + str(content))

        rep = Git(self.dirname)
        rep.clone(".", self.wcname)

        git = Git(self.wcname)
        wc = Repo(self.wcname)

        for b in wc.tree().contents:
            os.remove(self.wcname + "/" + b.name)

        self.writeContent(content)

        git.add("--ignore-errors", ".")
        if git.diff("--cached"):
            git.commit("-a", message="web edit")
            git.push("--all", repo=self.dirname)

        shutil.rmtree(self.wcname)

    def writeContent(self, content):
        for pos, name, body, language in content:
            fname = name
            if self.isDefaultName(fname):
                fname = self.createDefaultName(pos, language)
            f = open(self.wcname + "/" + fname, "w")
            print >>f, body
            f.close()

    def isDefaultName(self, name):
        return not name or name.startswith("pastefile")

    def createDefaultName(self, pos, language):
        return "pastefile" + str(pos) + "." + language
