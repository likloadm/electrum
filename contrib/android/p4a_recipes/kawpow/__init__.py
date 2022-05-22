from pythonforandroid.recipe.kawpow import KawpowPythonRecipe

assert KawpowPythonRecipe._version == "1.0"
assert KawpowPythonRecipe.depends == ['setuptools', 'python3', 'cffi', 'pycparser']
assert KawpowPythonRecipe.python_depends == []


class Kawpow(KawpowPythonRecipe):
    version = 'master'
    url = 'https://github.com/RavenCommunity/cpp-kawpow/archive/{version}.zip'
    site_packages_name = 'kawpow'


recipe = Kawpow()