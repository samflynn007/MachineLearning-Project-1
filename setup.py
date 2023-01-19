from setuptools import setup
from typing import List

# declaring variables for setup function
PROJECT_NAME = "housing-predictor" 
VERSION = "0.0.1"
AUTHOR = "Venkatesh Nellore"
DESCRIPTION = "This is My First END-TO-END ML PROJECT"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

''

"""
Desccription : This function is going to return list of requirements
mention in requirement.txt file
return: this function is going to return a list which contain name of libraries mentioned requirement .txt file
"""

def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
     return requirement_file.readlines()
 
''

   
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
    
)
      

    