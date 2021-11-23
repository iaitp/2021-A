'''
test cpu_util.py functionality is correct
'''
# Author: Matt Clifford <matt.clifford@bristol.ac.uk>
import time
import energy_monitor
import os

def test_args():
    tdp = 20
    inter = 0.1
    energy_monitor.utils.dummy_compute(2)
    m = energy_monitor.cpu_percent.monitor_cpu_percent(TDP=tdp, interval=inter)
    assert m.TDP == tdp
    assert m.interval == inter

if __name__ == '__main__':
    test_args()
