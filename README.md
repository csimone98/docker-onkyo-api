# Onkyo API
This is a RESTFull API for running commands on network-enabled Onkyo receivers based on [onkyo-eiscp](https://github.com/miracle2k/onkyo-eiscp) library. This is a forked project. This update features Python 3.14 and Fast API for communication but currently lacks in features w/o more code.

Currently fuctions for my Onkyo stereo for on off communication across two zones.

**TO DO**
BUILD OUT FAST API BEYOND THE ON/OFF AND SET SOURCE FEATURE


# Installation
## prerequisite
- [Docker](https://www.docker.com/)

## Building

    git clone https://github.com/csimone98/docker-onkyo-api.git
    cd docker-onkyo-api
    docker build --rm -t onkyo-api .

## Running     

    docker run -d -it -p 8000:8000 --net=host --name onkyo onkyo-api
    
# Usage

    GET http://localhost:8000/api/onkyo/<zone>

example

    GET http://localhost:8000/api/v1/onkyo/main
            -- this will turn the main zone on or off based on its current status and set a source 
