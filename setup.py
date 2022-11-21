from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gts_engine_client",
    version="0.1.2",
    description="gts_engine_client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/IDEA-CCNL/GTS-Engine-Client",
    author="pankunhao",
    author_email="pankunhao@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    exclude_package_date={'':['.gitignore']},
    install_requires=[
        'requests >= 2.27',
    ],

    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

