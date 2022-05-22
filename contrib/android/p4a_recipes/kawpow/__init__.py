from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class Kawpow(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'pip/archive/{version}.zip'
    site_packages_name = 'kawpow'
    depends = ['setuptools', 'cffi', 'pycparser']
    call_hostpython_via_targetpython = False


recipe = Kawpow()