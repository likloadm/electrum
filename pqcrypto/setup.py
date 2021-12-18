from setuptools import setup, Extension

tdc_yespower_module = Extension('pqcrypto',
                            sources = [
                                       'codec.c',
                                       'common.c',
                                       'fft.c',
                                       'fpr.c',
                                       'keygen.c',
                                       'pqclean.c',
                                       'rng.c',
                                       'sign.c',
                                       'vrfy.c',
                                       'sp800-185.c',
                                       'sha2.c',
                                       'randombytes.c',
                                       'fips202.c',
                                       'aes.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['./_sign', './common', './falcon-512'])

setup (name = 'pqcrypto',
       version = '0.1',
       author_email = 'tidecoins@protonmail.com',
       author = 'yarsawyer',
       url = 'https://github.com/yarsawyer/tdc_yespower',
       description = 'Bindings for yespower-1.0 proof of work used by tidecoin',
       ext_modules = [tdc_yespower_module])
