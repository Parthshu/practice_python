from setuptools import setup, find_packages
from typing import List


def get_requirments() -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst


setup(
    name="SampleProject_python",
    version="0.0.1",
    author="Parth Shah",
    author_email="parth.msu2017@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
)
