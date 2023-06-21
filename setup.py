from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:#we will provide a file path and the return value will be a list
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#when we read lines in requirements.txt /n will get added so we need to replace it
        requirements=[req.replace('/n','')for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

setup(
    name='mlproject',
    version='0.0.1',
    author='amrit',
    author_email='amritsairamp@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #it will go to the requirements.txt files and whatever is written there it will go and install that
    )

##now we will create src find so that it will find out how many packages are there 