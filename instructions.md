# create a virtual env
python3.6 -m venv /var/virtual_envs/service_registry

# get into the venv
source /var/virtual_envs/service_registry/bin/activate

# install the packages
pip install -r requirements.txt

# run the project
python app.py
