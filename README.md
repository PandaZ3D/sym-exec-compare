# Comparing Symbolic Execution Tools
Experiments for comparing symbolic execution tools Manticore and angr. Results are collected from the output of `perf stat`.

# Setup Configuration
apt-get update
apt-get upgrade

## Mantocire Dependencies

## angr Dependencies
apt-get install python3-dev libffi-dev build-essential virtualenvwrapper

## perf
`apt install linux-tools-common && apt get linux-tools-`uname -r``

## Python Version
Python 3.6.9

For running these pieces of software I recommend python virtual environments. Instructions can be found here. In my case I had to use `sudo apt-get install python3-venv`.

## Symbolic Execution Tools
* Manticore
* angr

## Benchmarking
* perf
