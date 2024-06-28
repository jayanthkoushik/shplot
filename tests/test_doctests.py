from doctest import DocFileSuite

import shplot

DOCTEST_MODULES = {shplot: []}  # type: ignore
DOCTEST_FILES = ["../README.md"]


def load_tests(loader, tests, ignore):
    for mod, modfiles in DOCTEST_MODULES.items():
        for file in modfiles:
            tests.addTest(DocFileSuite(file, package=mod))

    for file in DOCTEST_FILES:
        tests.addTest(DocFileSuite(file))

    return tests
