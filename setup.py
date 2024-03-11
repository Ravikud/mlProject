### This file builds the entire app as a package.

from setuptools import find_packages,setup
#Finds all the in the packages in the entire app

from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        this function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: # file_obj as temporary obj
        requirements=file_obj.readlines()#Read contents line by line
        ###\n replaced with blank space needs to remove for next line in requirements.txt file
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            ### remove the -e . from this file
    return requirements
          

setup(
    name='mlproject',
    version='0.0.1',
    author='Ravi',
    author_email='ravinampad@gmail.com',
    install_requires=get_requirements('requirements.txt')
)

