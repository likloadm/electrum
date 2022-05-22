from pythonforandroid.recipe import PythonRecipe


class Kawpow(PythonRecipe):
    version = 'master'
    url = 'https://github.com/RavenCommunity/cpp-kawpow/archive/{version}.zip'
    site_packages_name = 'kawpow'
    depends = ['setuptools']


recipe = Kawpow()