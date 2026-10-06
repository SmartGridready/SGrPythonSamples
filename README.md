# SmartGridready Python Samples

## Index

- [Summary](#summary)
- [Related Projects](#related-projects)

## Summary

[SGrPythonSamples](https://github.com/SmartGridready/SGrPythonSamples) provides sample projects that demonstrate the use of the _Communication Handler Library_ provided in [SGrPython](https://github.com/SmartGridready/SGrPython).  
The samples show different use cases of communicating with _products_, e.g. electricity meters, heat pumps, charging stations or PV inverters,
with the help of [external interface descriptions](https://library.smartgridready.ch/Device).

## Installation

### Requirements / Prerequisites

- Python interpreter >= 3.9, < 3.13

### Clone

Clone this repository to a new directory: <https://github.com/SmartGridready/SGrPythonSamples.git>

### Build and Run

The sample project uses [virtual environments](https://docs.python.org/3/tutorial/venv.html) and [pip](https://packaging.python.org/en/latest/key_projects/#pip) to manage dependencies.

Create and/or activate virtual environment in your project directory:

```bash
python -m venv .venv

# On Linux call this:
source ./.venv/bin/activate

# On Windows call this:
.\.venv\Scripts\Activate.ps1
```

While the virtual environment is active, packages will be installed inside the virtual environment, keeping your system and user directory clean.

Install the required dependencies from `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

After all dependencies have been installed, you may launch any of the samples:

```bash
python sample_xxx.py
```

## Related Projects

### OpenCEM

_OpenCEM_ is a simple implementation of an EMS developed at [FHNW](https://www.fhnw.ch), demonstrating the use of the _Communication Handler Library_.

The _OpenCEM_ project has been removed from the sample repository and moved to its own repository.  
You can find the source code at [OpenCEM](https://github.com/open-cem/open-cem).
