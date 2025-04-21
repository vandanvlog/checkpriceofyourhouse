from setuptools import find_packages,setup
from typing import List
 
HYPEN_e_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    # this is funciotn will return list of requirements here 
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n", " " )for req in requirements]

        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)
    
    return requirements

setup(
name ='house prices',
version='0.0.1',
author='vandan',
author_email='vandanprajapati2276@gmail.com',
packages=find_packages(),
instal_requires=get_requirements('requirements.txt')

)