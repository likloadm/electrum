from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class Ethash(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://github.com/RavenCommunity/cpp-kawpow/archive/{version}.zip'
    site_packages_name = 'ethash'
    depends = ['setuptools', 'cffi', 'pycparser']
    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True


recipe = Ethash()