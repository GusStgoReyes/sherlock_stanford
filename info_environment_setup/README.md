# Python Environment Setup

This guide will walk you through the steps to set up a Python environment on Sherlock.

## Step 1: Install Python

Based on the Python version that you might need, you can load it into Sherlock. Check [this website](https://www.sherlock.stanford.edu/docs/software/list/#devel) to determine the python versions available. 

```
ml python/<version>
```

## Step 2: Verify Python Installation

After installing Python, open a terminal or command prompt and type the following command to verify the installation:

```bash
python --version
```

If the command returns the Python version number, it means Python is installed correctly.

## Step 3: Set Up a Virtual Environment with venv (Highly recommended)

Setting up a virtual environment is recommended to keep your Python projects isolated. To create a virtual environment, open a terminal or command prompt and run the following command:

```bash
cd < /path/to/save/environment >
python -m venv myenv
```

Replace `myenv` with the desired name for your virtual environment. Remember the path where you save

To activate the virtual environment, run the following:

```bash
source < /path/to/save/environment >/myenv/bin/activate
```

## Step 4: Install Packages

Once your Python environment is set up, you can start installing packages using the package manager `pip`. To install a package, run the following command:

```bash
pip install package_name
```

Replace `package_name` with the name of the package you want to install.

## Step 5: Create a Requirements File (Optional)

If you are working on a project that requires specific packages, it's a good practice to create a requirements file. This file lists all the packages needed for your project. To create a requirements file, run the following command:

```bash
pip freeze > requirements.txt
```

This will create a file named `requirements.txt` containing a list of installed packages and their versions.

## Conclusion

You have successfully set up a Python environment on your machine. Note that if you need access to different softwares via Sherlock, you can load them. Maybe a section can be written about this. But follow this (website)[https://www.sherlock.stanford.edu/docs/software/modules/]. 
