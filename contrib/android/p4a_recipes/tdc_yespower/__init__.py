from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class TdcYespower(CompiledComponentsPythonRecipe):

    site_packages_name = 'tdc_yespower'
    depends = ['setuptools']


recipe = TdcYespower()