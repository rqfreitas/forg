import setuptools

setuptools.setup(
    include_package_data = True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.csv"],    
    }
)
