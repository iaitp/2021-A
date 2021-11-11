'''
test functions to analyse energy monitoring wrapper to intel power gadget
'''
# Author: Matt Clifford <matt.clifford@bristol.ac.uk>

import os
import platform
import pytest
import energy_monitor

def test_name():
    monitor = energy_monitor.monitor(name='energy1')
    assert monitor.name == 'energy1'

def test_standard_input():
    # standard input args
    monitor = energy_monitor.monitor()
    if platform.system() == 'Windows':
        assert monitor.bin == '"C:\\Program Files\\Intel\\Power Gadget 3.6\\IntelPowerGadget.exe"'

def test_non_standard_input():
    # non standard file location
    monitor = energy_monitor.monitor(non_standard_binary_path='/bin/loc.bin')
    assert monitor.bin == '/bin/loc.bin'

def test_arg_non_standard_binary_path_error():
    # # test error for non string
    args=[True, 0.1]
    for arg in args:
        with pytest.raises(ValueError) as val_error:
            monitor = energy_monitor.monitor(non_standard_binary_path=arg)
        assert str(val_error.value) == 'argument: non_standard_binary_path={arg} needs to be type str'.format(arg=repr(arg))

def test_joules_value():
    monitor = energy_monitor.monitor()
    monitor.start()
    energy_monitor.utils.dummy_compute(2)
    monitor.stop()
    assert type(monitor.joules) == float

def test_csv_removed():
    monitor = energy_monitor.monitor()
    monitor.start()
    energy_monitor.utils.dummy_compute(2)
    monitor.stop()
    assert os.path.exists(monitor.csv_file) == False

def test_os_support_error():
    monitor = energy_monitor.monitor()
    os_args = ['random-os', 'Linux']
    for arg in os_args:
        monitor.system_os = arg
        with pytest.raises(OSError) as OS_error:
            monitor.locate_bin()
        assert str(OS_error.value) == 'Intel Power Gadget not support on operating system: {arg}'.format(arg=repr(arg))
