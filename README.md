
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



# Backend Flask Server

This is a simple `hello world` type OOP Flask application that can be used as a template for multiple uses.

Two endpoints with calls to a separate class returning JSON employee data to client.

Features:
* Flask v2.0.2
* Simple OOP
* 2 defined endpoints

## Installation

### Prerequisite for Python Flask Server
* To do development through Docker only:
  * [Docker](https://docs.docker.com/get-docker/)
* To do development outside of Docker containers:
  * [python3](https://www.python.org/downloads/)
  * [pip3](https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/)

### Downloading this code from this repo
1. Create a directory to save the code:
   ```
   mkdir Workspace
   cd Workspace
   ```
2. Download this repo:
   ```
   git clone https://github.com/spaceshiptrip/DevSeries-Backend-Flask.git
   ```

## Build and Execute
* Change to the project directory
  ```
  cd DevSeries-Backend-Flask
  ```

### Building and Running with Docker
**Note: This is not necessary if you are not using Docker.**

* Build the docker container:
  ```
  docker build -t be:dev .
  ```

* Run the app through the container:
  ```
  docker run -it --rm -v $(PWD):/app -p 5000:5000 -e CHOKIDAR_USEPOLLING=true --name be --rm be:dev
  ```

### Non Dockerized Version
* Pre-requisites: 
  * Python 3
  * Pip 3

* Optional to run in [virtual env](https://docs.python-guide.org/dev/virtualenvs/)
  * Run the command to get into the virtual env
    ```
    source bin/activate
    ```
  * If errors are seen, run the command:
    ```
    rm -fr ./bin
    ```
    And install the virtualenv through the [docs](https://docs.python-guide.org/dev/virtualenvs/) 
  
* Build the server
  ```
  pip3 install -r requirements.txt
  ```
* Run the server
  ```
  python3 app.py
  ```
## Post Startup

### Test server response
Test with either cURL commands:

* cURL ([Windows](https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows)  [MacOS](https://idratherbewriting.com/learnapidoc/docapis_install_curl.html#:~:text=at%20paligo.net.-,Install%20curl%20on%20Mac,curl%20is%20probably%20already%20installed.))
  ```
  curl http://localhost:5000/getSomeData
  curl http://localhost:5000/getSomeDataFromFile
  ```

## Stopping Server
* Dockerized version
  * Open a terminal prompt
  * If you used the run command listed above:
    ```
    docker stop be
    ```
  * Replace `be` if you chose another name which can be found for port `5000`:
    ```
    docker ps
    ```
* Non Dockerized version
  * In the terminal running the server, press \<CTRL\>-c

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/issues/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[contributors-url]: https://github.com/spaceshiptrip/TechInterview-Backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[forks-url]: https://github.com/spaceshiptrip/TechInterview-Backend/network/members
[issues-shield]: https://img.shields.io/github/issues/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[issues-url]: https://github.com/spaceshiptrip/TechInterview-Backend/issues
[license-shield]: https://img.shields.io/github/license/spaceshiptrip/DevSeries-Backend-Flask?style=for-the-badge
[license-url]: https://github.com/spaceshiptrip/DevSeries-Backend-Flask/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaytorres-robotics/
[product-screenshot]: images/screenshot.png
