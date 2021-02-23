from distutils.core import setup
import py2exe

setup(console=[{ "script": "py_test.py"}],
      options={"py2exe": {
            "packages": ['py']}})