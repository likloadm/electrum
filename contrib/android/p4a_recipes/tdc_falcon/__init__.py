from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class TdcFalcon(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://github.com/yarsawyer/tdc_falcon/archive/{version}.zip'
    site_packages_name = 'tdc_falcon'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True

recipe = TdcFalcon()