This Python script queries an IP address against the [proxycheck.io](http://proxycheck.io/) API and retrieves information about the IP including whether it's a proxy, VPN, its ASN and node information. It then outputs the response in a pretty and syntax-highlighted JSON format.

Multiple IPs can be queried, which will result in a sequential query for each IP, returning an individual JSON output for each one.

<b>Example output:<b><br><br>
<img src="https://github.com/jacobstickney/pcheck/assets/86248382/0c4b69fd-e288-4dcd-81b2-3d2c6a2ff8dc" width="750">

## Installation

### Linux (via Git)
1. Make sure you have Git installed on your system. If not, you can install it using the following command:
```
sudo apt install git
```
<br>

2. Clone the repository from GitHub using the following command:
```
git clone https://github.com/jacobstickney/pcheck
```
<br>

3. Navigate into the cloned repository
```
cd pcheck
```
<br>

4. Make sure you have Python installed on your system. Most Linux distributions already have Python installed by default. You can check your Python version by running ```python --version``` or ```python3 --version``` in your terminal. If it's not installed, use your distribution's package manager to install Python.
<br>

5. Install ```pip```, which is the package installer for Python. You can do this by running the following command in your terminal:
```
sudo apt install python3-pip
```
<br>

6. Install the required Python libraries. You can do this by running the following command in your terminal:
```
pip3 install requests pygments colorama
```
<br>

6. Run the Python script in your terminal with the following command:
```
python3 pcheck.py
```
<br>

### Windows
1. Make sure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/). During installation, make sure to check the box that says "Add Python to PATH".
<br>

2. Open the Command Prompt.
<br>

3. Install ```pip```, which is the package installer for Python. You can do this by running the following command in your Command Prompt:
```
py -m ensurepip --upgrade
```
<br>

4. Install the required Python libraries. You can do this by running the following command in your Command Prompt:
```
py -m pip install requests pygments colorama
```
<br>

5. If you want to use Git to download the Python script, first make sure you have Git installed. If not, you can download it from [here](https://git-scm.com/download/win). Then clone the repository from GitHub using the following command:
```
git clone https://github.com/jacobstickney/pcheck
```
<br>

6. Navigate into the cloned repository. For instance, if the repository is saved in the "Documents" folder, you would use:
```
cd Documents\pcheck
```
<br>

7. Run the Python script in your Command Prompt with the following command:
```
py pcheck.py
```

