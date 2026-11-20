from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
# when i will run the requirements.txt file to install the packages
# simultaneouly the setup.py should also run so that it builds the packages
# -e . is just a token of connection to the setup.py file
# it is a short form for editable 
# it give live code updates
# clean imports and single command setup


# this specifies that my func will return a list with str
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # there will be a /n at the last of each package name
        requirements=[req.replace('/n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
        


setup(
    name='mlproject',
    version='0.0.1',
    author='amanpatel',
    author_email='amanpatel020804@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')



)