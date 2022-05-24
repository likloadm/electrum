from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class Kawpow(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://files.pythonhosted.org/packages/2f/43/985379652c61953f4206a8c7eae56e670e1db62b3e3a89ca2d24528be90e/kawpow-0.9.4.4.tar.gz'
    site_packages_name = 'kawpow'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True

recipe = Kawpow()