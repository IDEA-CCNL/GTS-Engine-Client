from setuptools import setup, find_packages

setup(
    name="gts_engine_client",
    version="0.1.0",
    description="gts_engine_client",
    long_description="client sdk for git_engine development suite",
    license="MIT Licence",
    url="https://idea.edu.cn",
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
)
