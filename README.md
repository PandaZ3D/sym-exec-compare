# Comparing Symbolic Execution Tools
Experiments for comparing symbolic execution tools Manticore and angr. Results are collected from the output of `perf stat`.

# Setup Configuration
apt-get update
apt-get upgrade

Additional dependencies for the tools or running benchmarks are detailed below.

## Python Version
Python 3.6.9

For running these pieces of software I recommend python virtual environments. I used `virtualenvwrapper` which is an extended package built on python virtual environments. Documentation can be found here (venvwrapper). Install with `apt-get install virtualenvwrapper`

# Symbolic Execution Tools
* angr
* Manticore

## Installing angr
angr requires these dependencies before installation:
```
apt-get install python3-dev libffi-dev build-essential virtualenvwrapper
```
To install angr use `mkvirtualenv --python=$(which python3) angr && python -m pip install angr`

## Installing Mantocire

# Benchmarking
* perf (wiki link)
* Logic Bombs (reference)

## perf
`apt install linux-tools-common && apt get linux-tools-`uname -r``

## Logic Bombs
When working with this software, make sure that the required dependencies are installed. Instructions can be found [here](https://github.com/hxuhack/logic_bombs#dependencies). 

To get a version of the scripts that have benchmarks for manticore, checkout the branch from the [pull request](https://github.com/hxuhack/logic_bombs/pull/14).
```
git fetch origin pull/14/head
git checkout -b pullrequest FETCH_HEAD
```
