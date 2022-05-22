from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class Kawpow(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://github.com/RavenCommunity/cpp-kawpow/archive/{version}.zip'
    site_packages_name = 'kawpow'
    depends = ['setuptools', "cffi", "pycparser"]
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['LDFLAGS'] += ' -lc++_shared'
        return env

    def should_build(self, arch):
        return True


recipe = Kawpow()