# idm_id
This is a repository containing the files of DSSS.

## Installation instructions

  pip install git+https://github.com/haaguileraa/idm_id
  
## Functionalities

`imshow` - shows an image in a Jupyter notebook

## Repo's structure


`idm_id`             # Main folder
.
├── mypackage        
│  ├── __init__.py  
│  ├── function.py  
├── setup.py         
├── requirements.txt 
├── README.md        
├── .gitignore       

.
├── mypackage        # Folder containing our set of functions
│  ├── __init__.py   # File used to indicate that this folder contains a Python package.
│  ├── function.py   # File containing our functions
├── setup.py         # You have to generate a set-up to ensure the functioning of your package
├── requirements.txt # You can also intstall packages using this file and the command line: ```pip install -r requirements.txt```
├── README.md        
├── .gitignore       # Useful file which contains the folders/scripts that you don't want to push in your repo, but you are using locally.