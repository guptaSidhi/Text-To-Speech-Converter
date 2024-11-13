from setuptools import find_packages, setup
from typing import List

requirements_file = 'requirements.txt'
HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    with open(requirements_file) as requirement_file:
        requirements = requirement_file.readlines()
        requirements_list = [requirement.replace("\n","") for requirement in requirements]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
    return requirements_list


setup(
    name = "Text To Speech Converter",
    version = "0.0.1",
    author = "Sidhi Gupta",
    author_email = "guptasidhi159@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)