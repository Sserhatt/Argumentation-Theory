from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


TEXT_TYPES = {
    "text/plain",
    "text/html",
    "text/css",
    "text/csv",
    "text/xml",
    "text/txt",
    "text/tsv",
    "application/xml",
    "application/javascript",
    "text/javascript",
    "application/json",
    "application/yaml",
    "text/yaml",
}


class UTF8StaticHandler(SimpleHTTPRequestHandler):
    def send_header(self, keyword, value):
        if keyword.lower() == "content-type":
            base_type = value.split(";", 1)[0].strip().lower()
            if "charset=" not in value and base_type in TEXT_TYPES:
                value = f"{base_type}; charset=utf-8"
        super().send_header(keyword, value)


if __name__ == "__main__":
    server = ThreadingHTTPServer(
        ("0.0.0.0", 8000),
        partial(UTF8StaticHandler, directory="/app"),
    )
    server.serve_forever()
