FROM osgeo/gdal:ubuntu-small-3.6.0

# Install dependencies
RUN apt-get update && apt-get install libc++-dev python3-pip -y

RUN mkdir /app && cd /app

# Activate your virtual environment
RUN python3 -m pip install GDAL==3.6.0 centerline
RUN whereis centerline