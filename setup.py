#!/usr/bin/env python
"""
FIXME:
    incoporate unix_build / mingw_build into this script
    ensure libsver.so installs correctly

CommandLine:
    python -c "import utool, vtool; utool.checkpath(vtool.__file__, verbose=True)"
    python -c "import utool, vtool; utool.checkpath(utool.unixjoin(utool.get_module_dir(vtool), 'libsver.so'), verbose=True)"
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from setuptools import setup
from os.path import dirname  # NOQA
import six

#import cyth

#cyth.translate('vtool/keypoint.py')
#cyth.translate('vtool/keypoint.py', 'vtool/spatial_verification.py')


def native_mb_python_tag():
    import sys
    import platform
    major = sys.version_info[0]
    minor = sys.version_info[1]
    ver = '{}{}'.format(major, minor)
    if platform.python_implementation() == 'CPython':
        # TODO: get if cp27m or cp27mu
        impl = 'cp'
        if ver == '27':
            IS_27_BUILT_WITH_UNICODE = True  # how to determine this?
            if IS_27_BUILT_WITH_UNICODE:
                abi = 'mu'
            else:
                abi = 'm'
        else:
            abi = 'm'
    else:
        raise NotImplementedError(impl)
    mb_tag = '{impl}{ver}-{impl}{ver}{abi}'.format(**locals())
    return mb_tag


def parse_version():
    """ Statically parse the version number from __init__.py """
    from os.path import dirname, join  # NOQA
    import ast
    init_fpath = join(dirname(__file__), 'vtool', '__init__.py')
    with open(init_fpath) as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)
    class VersionVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                try:
                    if target.id == '__version__':
                        self.version = node.value.s
                except AttributeError:
                    pass
    visitor = VersionVisitor()
    visitor.visit(pt)
    return visitor.version

DEV_REQUIREMENTS = [
    'atlas',
]


INSTALL_REQUIRES = [
    'cython >= 0.21.1',
    'numpy >= 1.9.0',
    'scipy >= 0.18.0',
    'scikit-learn >= 0.16.1',
    'statsmodels >= 0.6.1',
    #'cv2',  # no pipi index
]

TEST_APT_REQUIRES = [
    #sudo apt-get install libjpeg-turbo8-dev
    'lcms2-dev'  # sudo apt-get install liblcms2-dev
]

TEST_PIP_REQUIRES = [
    'smc.freeimage',  # sudo pip install smc.freeimage
]

CLUTTER_PATTERNS = [
    'libsver.*'
]

NAME = = 'vtool'
MB_PYTHON_TAG = native_mb_python_tag()  # NOQA
VERSION = parse_version()

if six.PY2:
    INSTALL_REQUIRES += ['functools32 >= 3.2.3-1']

if __name__ == '__main__':
    import utool as ut
    from utool import util_setup
    kwargs = util_setup.setuptools_setup(
        setup_fpath=__file__,
        name=NAME,
        packages=util_setup.find_packages(),
        version=VERSION,
        license=util_setup.read_license('LICENSE'),
        long_description=util_setup.parse_readme('README.md'),
        ext_modules=util_setup.find_ext_modules(),
        cmdclass=util_setup.get_cmdclass(),
        description=('Vision tools - tools for computer vision'),
        url='https://github.com/Erotemic/vtool',
        author='Jon Crall',
        author_email='erotemic@gmail.com',
        keywords='',
        install_requires=INSTALL_REQUIRES,
        clutter_patterns=CLUTTER_PATTERNS,
        # package_data={'build': ut.get_dynamic_lib_globstrs()},
        # build_command=lambda: ut.Repo(dirname(__file__)),
        build_command=lambda: ut.std_build_command(),
        classifiers=[],
    )
    setup(**kwargs)

#from Cython.Build import cythonize
#from Cython.Distutils import build_ext

#python -c "import pyximport; pyximport.install(reload_support=True, setup_args={'script_args': ['--compiler=mingw32']})"

#extensions = [Extension('vtool/linalg_cython.pyx')]
#extensions = cythonize('vtool/*.pyx')
#[
#    Extension('vtool.linalg_cython', ['vtool/linalg_cython.pyx'],
#              include_dirs=[np.get_include()])
#]
#r'''
#set PATH=%HOME%\code\utool\utool\util_scripts;%PATH%
#cyth.py vtool\linalg_cython.pyx
#cd %HOME%\code\vtool
#python %HOME%/code/vtool/vtool/tests/test_linalg.py
#ls vtool/*_cython*
#python setup.py build_ext --inplace && python vtool/tests/test_linalg.py
#python
#python -c "import utool; utool.checkpath('vtool/linalg_cython.pyd', verbose=True)"
#cyth.py %HOME%/code/vtool/vtool/linalg_cython.pyx
#'''
#ext_modules = cythonize("vtool/linalg_cython.pyx")
