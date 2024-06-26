from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'

# .)The blw fun will return a list of string of requirements.
# .0While reading requimnt file -e . will also come so apply condition to removwe it .
def get_requirements(file_path:str)->List[str]:
  requirements=[]
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  return requirements

    

setup(
  name='mlproject',
  version='0.0.1',
  author='Subhan',
  author_email='subhansheikh5843@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt'),
)