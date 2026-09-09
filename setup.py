from setuptools import setup, find_packages

setup(
    name="my-python-app",
    version="1.0.0",
    py_modules=["app"],
    install_requires=[
        "Flask>=3.0"
    ],
)
