from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class ArlDilithium(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://github.com/liklo_adm/arl_dilithium/archive/{version}.zip'
    site_packages_name = 'arl_dilithium'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True

recipe = ArlDilithium()