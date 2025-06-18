'''
The setup.py file is an essential part of packaging and distributing Python projects.
It is used by setuptools(or distutils in older Python versions) to define the configurations of your Project.
It includes metadata about the project, such as its name, version, author, license, and dependencies.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements from a file and returns them as a list.
    
    Args:
        file_path (str): The path to the requirements file.
        
    Returns:
        List[str]: A list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read the requirements from the file
            lines = file.readlines()
            # Process the lines to remove comments and empty lines
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and "-e."
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Returning an empty list.")
        
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Nikunj Kichambare',
    author_email='kichambare.nikunj@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
