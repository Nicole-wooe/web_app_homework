from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        with open("templates/contacts.html",
                  "r",
                  encoding="utf-8") as file:

            html_content = file.read()

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            html_content.encode("utf-8")
        )

    def do_POST(self):

        content_length = int(
            self.headers["Content-Length"]
        )

        post_data = self.rfile.read(
            content_length
        ).decode("utf-8")

        parsed_data = parse_qs(post_data)

        print("Получены данные:")

        for key, value in parsed_data.items():
            print(f"{key}: {value}")

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            "Форма успешно отправлена".encode("utf-8")
        )


server = HTTPServer(
    ("localhost", 8000),
    SimpleHTTPRequestHandler
)

print("Сервер запущен:")
print("http://localhost:8000")

server.serve_forever()
