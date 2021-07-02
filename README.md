![BLOGG Log](assets/blog_logo.png)   
This is a simple blogging app backend built with FastAPI.
This project is created to simulate a real CRUD blogging system.
It is built to be used by several system hence adopting the REST APIs aproach.
Just like all REST APIs you can perform all functions of this system using the endpoints we created.
Everything is simple and easy to use no need to read the code to understand, though you can still jump in there to 
make some modifications.

![Work FLow](https://github.com/lokaimoma/BLOGG/actions/workflows/run_test.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/lokaimoma/BLOGG/blob/main/LICENSE)

### Requirements
- - -
+ [Python 3](https://www.python.org/downloads/)

### How to install
- - -
+ #### Download and install python. 
  The versin should be greater than or equal to version 3.6
+ #### Clone the project unto your pc.
```
git clone https://github.com/lokaimoma/BLOGG.git
```
+ #### Change directory to the project directory.
```
cd BLOGG
```
+ #### Create a virtual environment.
    + ##### Windows
    ```
    python -m venv venv
    ```
    + ##### Linux and Mac OS
    ```bash
    python3 -m venv venv
    ```
+ #### Activate the virtual environment.
    + ##### Windows
        + cmd
        ```
        .\venv\Scripts\activate
        ```
        + powershell
        ```
        .\venv\Scripts\Activate.ps1
        ```
    + ##### Linux and Mac OS
    ```bash
    Source venv/bin/activate
    ```
+ #### Install all the requirements.
```bash
pip install -r requirements.txt
```
+ Set an environmental variable pointing to you database url (KEY = DATABASE_URL)
 ```
 FORMAT: DATABASE_URL=sqlite+aiosqlite:///db-dev.sqlite
 ```
 A detail doc will be created showing the format for different databases.
+ ##### Deactivate the environment with the command below.
```
deactivate
```
+ #### Reactivate the environment again. Check above for plateform
  specific steps.
+ #### Run this command to create the database
```
alembic upgrade head
```
+ #### You can now run the program with the command below.
    + ##### Windows
    ```
    python engine.py
    ```
    + ##### Linux and Mac OS
    ```
    python3 engine.py
    ```
 + #### By default the app runs on [localhost:8000](#)

### Documentation
- - -
To read the docs for api, start the app and open the location [http://localhost:8000/docs](#)
to read detailed documentation of the endpoints and how to use them.

### License
- - - 
```
      
MIT License

Copyright (c) 2021 Owusu Kelvin Clark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
