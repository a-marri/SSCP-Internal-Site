#!/usr/bin/env python3
"""
Simple HTTP server to serve the GitBook content locally.
"""

import os
import sys
import argparse
import http.server
import socketserver
from pathlib import Path


def serve_gitbook(gitbook_dir, port=8000):
    """
    Serve the GitBook content locally using a simple HTTP server.
    
    Args:
        gitbook_dir (str): Path to the GitBook directory
        port (int): Port to serve on
    """
    # Check if the GitBook directory exists
    if not os.path.isdir(gitbook_dir):
        print(f"Error: GitBook directory {gitbook_dir} does not exist")
        sys.exit(1)
    
    # Check if SUMMARY.md exists
    if not os.path.isfile(os.path.join(gitbook_dir, 'SUMMARY.md')):
        print(f"Warning: SUMMARY.md not found in {gitbook_dir}")
    
    # Create an index.html file that redirects to README.md
    index_path = os.path.join(gitbook_dir, 'index.html')
    if not os.path.isfile(index_path):
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>GitBook</title>
    <meta http-equiv="refresh" content="0; url=README.md">
</head>
<body>
    <p>Redirecting to <a href="README.md">README.md</a>...</p>
</body>
</html>
""")
    
    # Change to the GitBook directory
    os.chdir(gitbook_dir)
    
    # Create a custom request handler that sets the correct content type for markdown files
    class GitBookHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # If the path ends with .md, set the content type to text/markdown
            if self.path.endswith('.md'):
                self.send_response(200)
                self.send_header('Content-type', 'text/markdown')
                self.end_headers()
                with open(self.path[1:], 'rb') as f:
                    self.wfile.write(f.read())
            else:
                # Otherwise, use the default handler
                super().do_GET()
    
    # Create the server
    handler = GitBookHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    print(f"Serving GitBook at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")


def main():
    """
    Main function to run the server.
    """
    parser = argparse.ArgumentParser(description='Serve GitBook content locally')
    parser.add_argument('--gitbook', required=True, help='Path to the GitBook directory')
    parser.add_argument('--port', type=int, default=8000, help='Port to serve on')
    
    args = parser.parse_args()
    
    serve_gitbook(args.gitbook, args.port)


if __name__ == '__main__':
    main()
