import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


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


def parse_args():
    parser = argparse.ArgumentParser(
        description="Serve this repository with UTF-8 content headers."
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host interface to bind. Default: 0.0.0.0",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind. Default: 8000",
    )
    parser.add_argument(
        "--directory",
        default=None,
        help="Directory to serve. Defaults to /app when present, otherwise the current working directory.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    default_directory = Path("/app") if Path("/app").is_dir() else Path.cwd()
    directory = Path(args.directory).resolve() if args.directory else default_directory.resolve()

    server = ThreadingHTTPServer(
        (args.host, args.port),
        partial(UTF8StaticHandler, directory=str(directory)),
    )
    print(f"Serving {directory} on http://{args.host}:{args.port}")
    server.serve_forever()
