from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class TdcYespower(CompiledComponentsPythonRecipe):

    site_packages_name = 'tdc_yespower'
    depends = ['setuptools']

    call_hostpython_via_targetpython = False

    def should_build(self, arch):
        return True


recipe = TdcYespower()