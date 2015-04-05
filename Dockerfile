FROM        ubuntu:14.04

RUN         apt-get update
RUN         apt-get -y upgrade
RUN         apt-get -y install g++
RUN         apt-get -y install make
RUN         apt-get -y install curl
RUN         apt-get -y install git
RUN         apt-get -y install python-dev
RUN         export LD_LIBRARY_PATH=/usr/local/lib
RUN         cd /home && curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py

WORKDIR     /home
RUN         mkdir /home/atelierlaurier
COPY        . /home/atelierlaurier/
RUN         cd /home/atelierlaurier && pip install --editable .
RUN         mkdir -p /var/run/circus

EXPOSE      6543

WORKDIR     /home/atelierlaurier
CMD         /usr/local/bin/circusd /home/atelierlaurier/development.ini