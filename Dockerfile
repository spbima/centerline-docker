FROM osgeo/gdal:ubuntu-small-3.6.0

LABEL maintainer="Ivanko Mike <spbima@mail.ru>"

# Install packages
RUN apt-get update && apt-get install libc++-dev python3-pip -y

# Install python dependencies
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal/ && export C_INCLUDE_PATH=/usr/include/gdal/ && python3 -m pip install GDAL==3.6.0 centerline==0.6.4 geojson

# Add symlink
RUN ln -s /root/.local/bin/create_centerlines /usr/bin/create_centerlines

# Add HTTP server script
ADD http_server.py /app/http_server.py

EXPOSE 8000
CMD python3 /app/http_server.py
