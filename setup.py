from setuptools import find_packages,setup

from typing import List



HYPEN_E_DOT='-e .'
#the function should return a list of requirements
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        [req.replace('\n','') for req  in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        

setup(
    name="Data science project",
    version="0.0.1",
    author="Nizarkarkar",
    author_email="nizarkarkar2019@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements("requirements.txt")
    
)