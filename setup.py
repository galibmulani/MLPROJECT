from setuptools import find_packages,setup
from typing import List


HYPEN_N_DOT="-e ."
def get_requirements(file_path:str)->List:
    requirements=[]

    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_N_DOT in requirements:
            requirements.remove(HYPEN_N_DOT)

    return requirements;

setup(name="mlprojects",
      version="0.0.1",
      author="galib",
      author_email="mulanigalib1@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      )