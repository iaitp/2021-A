# Python Setup
Use either the automatic or manual setup process as described below

### Automatic Setup
Use the install script to set up automatically:
`$ ./install.sh`

### Manual Setup

1. Create conda venv:

`$ conda create --name energy_monitor python=3.8`

2. Activate venv:

`$ conda activate energy_monitor`

3. Install dependancies with pip:

`$ pip install -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html`

4. Install current dir in editable mode:

`$ pip install -e .`

# External Dependancies

We use [IntelPowerGadget](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html) to monitor energy usage on Windows/MacOS. 
