from pythonforandroid.recipe import PythonRecipe


class Ethash(PythonRecipe):
    version = 'master'
    url = 'https://github.com/RavenCommunity/cpp-kawpow/archive/{version}.zip'
    site_packages_name = 'ethash'
    depends = ['setuptools']


recipe = Ethash()