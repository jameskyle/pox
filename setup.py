import glob
import os

import pox.core
from setuptools import setup
from setuptools import find_packages


NAME="pox"
DESCRIPTION="POX is a networking software platform."


core = pox.core.initialize()
VERSION=".".join(map(str,core.version))

tools=glob.glob("tools/*")
exts=glob.glob("ext/*.py")
docs=['LICENSE', 'README', 'NOTICE']
pox_dir="pox-{0}".format(VERSION)
shares=os.path.join("usr", "share", pox_dir)

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      author="Murphy McCauley",
      url="http://www.noxrepo.org/",
      packages=find_packages(exclude=["tests", "tests.*"]),
      data_files=[
          (os.path.join(shares, 'tools'), tools),
          (os.path.join(core.library, 'ext'), exts),
          (os.path.join(shares, "doc"), docs),
      ],
      entry_points={
          'console_scripts': [
              'pox = pox.boot:boot',
          ],
      },
)
