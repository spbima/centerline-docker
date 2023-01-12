# centerline-docker
Docker image with HTTP API for centerline command-line tool [**centerline.readthedocs.io**](https://centerline.readthedocs.io).

Roads, rivers and similar linear structures are often represented by long and complex polygons. Since one of the most important attributes 
of a linear structure is its length, extracting that attribute from a polygon can prove to be more or less difficult.

This library tries to solve this problem by creating the the polygon's centerline using the Voronoi diagram.

## Installation

Pull docker image from Docker Hub and run container

.. code:: bash

    $ docker pull spbima/centerline
    $ docker run -d --name centerline spbima/centerline

Or you can use **docker-compose**

Create file ``docker-compose.yml``

.. code:: yaml
    version: '3'
    services:
      centerline:
        container_name: centerline
        image: spbima/centerline:0.6.4
        restart: always
        ports:
          - "8000:8000"

And run container by command

.. code:: bash

    $ docker-compose -f docker-compose.yml up -d


## Usage


