# bhptrojan

## Overview

`git_trojan.py` is a proof-of-concept Python tool inspired by the book "Black Hat Python". It demonstrates how a stealthy, modular trojan can be controlled and updated remotely using GitHub as a command-and-control (C2) infrastructure. This tool is intended for educational and penetration testing purposes only.

## Features
- **Modular Design:** Dynamically loads and executes modules from a remote GitHub repository.
- **Remote Configuration:** Retrieves configuration and modules from GitHub, allowing real-time updates and tasking.
- **Data Exfiltration:** Stores results of executed modules back to the repository in a stealthy manner.
- **Threaded Execution:** Runs multiple modules concurrently for efficiency and stealth.
- **Custom Importer:** Uses a custom Python importer to fetch and load code from GitHub on demand.

## How It Works
1. **Authentication:** Uses a GitHub personal access token (stored in `mytoken.txt`) to authenticate and interact with the repository.
2. **Configuration Fetch:** Downloads a JSON configuration file from the `config/` directory in the repository, specifying which modules to run.
3. **Module Loading:** For each module listed in the config, dynamically imports the module code from the `modules/` directory in the repository.
4. **Execution:** Runs each module in a separate thread and collects the results.
5. **Data Storage:** Encodes and uploads the results to the `data/` directory in the repository, using ISO-formatted timestamps for filenames.

## Usage

### Prerequisites
- Python 3.x
- `github3.py` library (`pip install github3.py`)
- A GitHub account and a personal access token with repo permissions

### Setup
1. **Clone or Download the Repository**
2. **Create a Personal Access Token**
   - Go to your GitHub account settings > Developer settings > Personal access tokens
   - Generate a token with `repo` permissions
   - Save the token in a file named `mytoken.txt` in the same directory as `git_trojan.py`
3. **Configure the Repository**
   - Add your module scripts to the `modules/` directory in the repository
   - Add a configuration JSON file (e.g., `abc.json`) to the `config/` directory specifying which modules to run

### Running the Trojan
```bash
python git_trojan.py
```

## Configuration File Example (`config/abc.json`)
```json
[
    {"module": "keylogger"},
    {"module": "screenshot"}
]
```

## Disclaimer
This tool is for educational and authorized penetration testing use only. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.

## Credits
- Inspired by "Black Hat Python" by Justin Seitz
- Uses the `github3.py` library for GitHub API interactions
