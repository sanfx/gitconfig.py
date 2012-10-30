import os
from lazy_dirs import lazy_dirs
from config import config


path = os.path.expanduser("~/git")
exists = os.path.exists(path)
dirs = lazy_dirs(os.path.expanduser("~/git"))