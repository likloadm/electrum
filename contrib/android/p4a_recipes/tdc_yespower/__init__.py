from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class TdcYespower(CompiledComponentsPythonRecipe):
    version = 'master'
    url = 'https://github.com/yarsawyer/tdc_yespower/archive/{version}.zip'
    site_packages_name = 'tdc_yespower'
    depends = ['setuptools']

    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True


recipe = TdcYespower()