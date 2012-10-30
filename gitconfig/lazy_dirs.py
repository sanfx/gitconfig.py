import os
from git import Repo


class dir():
    path = None
    repo = None

    def __init__(self, path):
        self.path = path
        try:
            self.repo = Repo(self.path)
        except:
            self.repo = None

    @property
    def status(self):
        """return git status"""
        if self.repo:
            return self.repo.git.status()

    @property
    def nothing_to_commit(self):
        """return True if nothing to commit"""
        return self.status.find("nothing to commit") > 0

    @property
    def untracked(self):
        """return list of untracked files"""
        return self.repo.untracked_files

    @property
    def deleted(self):
        """return list of deleted files"""
        return map(lambda d: d.a_blob.path,
                   self.repo.index.diff(None).iter_change_type("D"))

    @property
    def modified(self):
        """return list of modified files"""
        return map(lambda d: d.a_blob.path,
                   self.repo.index.diff(None).iter_change_type("M"))

    @property
    def name(self):
        return os.path.basename(self.path)

    @property
    def git(self):
        return self.repo is not None

    def __str__(self):
        #return "__str__"
        return str(self.path)


class lazy_dirs():
    path = None

    def __init__(self, path):
        self.path = path

    def dirs(self):
        dirs = []
        for parent, directories, files in os.walk(self.path, topdown=True):
            for directory in directories:
                path = os.path.join(parent, directory)
                dirs.append(dir(path))
            return dirs

    def __getslice__(self, i, j):
        return self.dirs()[i:j]

    def __iter__(self):
        for i in self[:]:
            yield i

    def __str__(self):
        return "\n".join(map(str, self[:]))