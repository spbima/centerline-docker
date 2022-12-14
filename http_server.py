from http.server import HTTPServer, BaseHTTPRequestHandler

import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from io import BytesIO
import geojson
import subprocess
import uuid

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(405)
        self.end_headers()

    def do_POST(self):
        content_type = self.headers['Content-Type']
        if content_type != 'application/json':
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"status": 400, "message": "Wrong Content-Type. Should be application/json."}')
            return

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        input = geojson.loads(body.decode("utf-8"))
        if not hasattr(input, 'is_valid') or not input.is_valid:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"status": 400, "message": "Wrong GeoJSON format."}')
            return

        data_directory = 'data'
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

        file_name = '/' + data_directory + '/' + str(uuid.uuid4()) + '.geojson'
        file_name_out = '/' + data_directory + '/output_' + str(uuid.uuid4()) + '.geojson'

        response = BytesIO()

        with open(file_name, "w") as geojson_file:
            geojson_file.write(body.decode("utf-8"))

        command = ['create_centerlines', file_name, file_name_out]

        exec_script = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = exec_script.communicate()


        if os.path.exists(file_name_out):
            with open(file_name_out, 'r') as file:
                responce_data = file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(responce_data))
        else:
            self.send_response(500)
            self.end_headers()
            responce_data = stdout
            self.wfile.write(responce_data)

        os.remove(file_name)
        os.remove(file_name_out)


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()