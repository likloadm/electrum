from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class TdcFalcon(CompiledComponentsPythonRecipe):

    site_packages_name = 'tdc_falcon'
    depends = ['setuptools']

recipe = TdcFalcon()