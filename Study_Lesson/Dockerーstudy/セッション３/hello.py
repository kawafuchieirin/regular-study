#!/usr/bin/env python3
"""
シンプルなHello Worldプログラム
コンテナ上で実行されるプログラムの例
"""

import os
import platform

def main():
    print("=" * 50)
    print("Hello from Docker Container!")
    print("=" * 50)
    print(f"Python version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Container hostname: {os.environ.get('HOSTNAME', 'N/A')}")
    print(f"Working directory: {os.getcwd()}")
    print("=" * 50)
    print("This program is running inside a Docker container!")
    print("=" * 50)

if __name__ == "__main__":
    main()

