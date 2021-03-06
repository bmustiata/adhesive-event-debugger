from setuptools import setup
from setuptools import find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name="adhesive_event_debugger",
    version="1.0.0",
    description="adhesive_event_debugger",
    long_description=readme,
    author="Bogdan Mustiata",
    author_email="bogdan.mustiata@gmail.com",
    license="BSD",
    entry_points={"console_scripts": ["adhesive_event_debugger = adhesive_event_debugger.mainapp:main"]},
    install_requires=[],
    packages=packages,
    package_data={"": ["*.txt", "*.rst"], "arst": ["py.typed"],},
)
