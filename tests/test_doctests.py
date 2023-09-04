from doctest import DocFileSuite

import shplot.profiles

DOCTEST_MODULES = {shplot.profiles: ["builtin.py", "_interface.py"]}


def load_tests(loader, tests, ignore):
    for module, modfiles in DOCTEST_MODULES.items():
        for modfile in modfiles:
            tests.addTests(DocFileSuite(modfile, package=module))
    return tests
