import setuptools 

setuptools.setup(   
    name = "intermediate-package",
    version = "1.0",
    packages = setuptools.find_packages(),

    install_requires = ['boto==2.3.0', 'intermediate-package']
)
