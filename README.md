# Cafe-Manager
## Overview
A project that acted as an introduction to Python during my time at a Generation bootcamp. In essence, this project was a cafe management system with requirements set by the product owner.

## Requirements
* CLI based
* Menus
  * Products
  * Orders
  * Courier
* Entry manipulation
  * Add 
  * Update 
  * Delete
* Persists data
  * Originally stored in CSV's however was moved to a database for accessiblity purposes. 
* Robust and readable code
  * Ensuring the code is easy to maintain by being readable, modular and with minimal errors.
 
## How to run
1 - Install Python from the official source
2 - Open the file location
3 - Create a venv 
```
    python -m venv .venv
OR
    python3 -m venv .venv
OR
    py -m venv .venv
```
4 - Activate the venv
```
Windows
    .venv/Scripts/Activate.ps1
Linux
    chmod .venv/bin/activate
    source .venv/bin/activate
```
5 - Install requirements
```
    python -m pip install -r requirements.txt
OR
    python3 -m pip isntall -r requirements.txt
OR
    py -m pip install -r requirements.txt
```
6 - Run the application
  ```
    python source/main.py
OR
    python3 source/main.py
OR
    py source/main.py
```
## Future improvements
* Admin account
  * Locking certain actions behind an administrative permission 
* First time setup
  * Admin account setup for specific actions
  * Configurable database parameters
* Unit testing
  * Ensuring all functions are robust

