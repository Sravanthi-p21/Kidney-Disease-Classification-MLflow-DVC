from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements'''

    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        return requirements
    
setup (
        name ='cnnlassifier',
        version= '1.0',
        packages=find_packages(),
        author='sravanthipaturi',
        author_email = 'paturisravanthi21@gmail.com',
        install_requires = get_requirements('requirements.txt')
    )