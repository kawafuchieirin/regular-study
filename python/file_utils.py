#!/usr/bin/env python3
"""
ファイル操作ユーティリティスクリプト
プロジェクト内のファイルを操作するための便利な関数を提供します
"""

import os
import sys
from pathlib import Path
from typing import List, Optional


def list_files(directory: str = ".", extension: Optional[str] = None) -> List[str]:
    """
    指定されたディレクトリ内のファイルを一覧表示します
    
    Args:
        directory: 検索するディレクトリパス（デフォルト: カレントディレクトリ）
        extension: フィルタリングする拡張子（例: '.py', '.md'）
    
    Returns:
        ファイルパスのリスト
    """
    directory_path = Path(directory)
    if not directory_path.exists():
        print(f"エラー: ディレクトリ '{directory}' が存在しません")
        return []
    
    files = []
    for file_path in directory_path.rglob("*"):
        if file_path.is_file():
            if extension is None or file_path.suffix == extension:
                files.append(str(file_path))
    
    return sorted(files)


def count_lines(file_path: str) -> int:
    """
    ファイルの行数をカウントします
    
    Args:
        file_path: ファイルパス
    
    Returns:
        行数
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"エラー: ファイル '{file_path}' を読み込めませんでした: {e}")
        return 0


def get_file_info(file_path: str) -> dict:
    """
    ファイルの情報を取得します
    
    Args:
        file_path: ファイルパス
    
    Returns:
        ファイル情報の辞書
    """
    path = Path(file_path)
    if not path.exists():
        return {}
    
    stat = path.stat()
    return {
        "path": str(path),
        "name": path.name,
        "size": stat.st_size,
        "lines": count_lines(file_path),
        "extension": path.suffix,
    }


def main():
    """メイン関数"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            # ファイル一覧を表示
            extension = sys.argv[2] if len(sys.argv) > 2 else None
            files = list_files(".", extension)
            print(f"\n見つかったファイル数: {len(files)}\n")
            for file in files:
                print(f"  {file}")
        
        elif command == "info":
            # ファイル情報を表示
            if len(sys.argv) < 3:
                print("使用方法: python file_utils.py info <ファイルパス>")
                return
            
            file_path = sys.argv[2]
            info = get_file_info(file_path)
            if info:
                print(f"\nファイル情報:")
                print(f"  パス: {info['path']}")
                print(f"  名前: {info['name']}")
                print(f"  サイズ: {info['size']} バイト")
                print(f"  行数: {info['lines']}")
                print(f"  拡張子: {info['extension']}")
            else:
                print(f"エラー: ファイル '{file_path}' が見つかりません")
        
        elif command == "count":
            # プロジェクト内のPythonファイルの行数をカウント
            python_files = list_files(".", ".py")
            total_lines = 0
            print(f"\nPythonファイル一覧:\n")
            for file in python_files:
                lines = count_lines(file)
                total_lines += lines
                print(f"  {file}: {lines} 行")
            print(f"\n合計: {total_lines} 行")
        
        else:
            print(f"不明なコマンド: {command}")
            print_usage()
    else:
        print_usage()


def print_usage():
    """使用方法を表示"""
    print("使用方法:")
    print("  python file_utils.py list [拡張子]     - ファイル一覧を表示")
    print("  python file_utils.py info <ファイル>   - ファイル情報を表示")
    print("  python file_utils.py count             - Pythonファイルの行数をカウント")
    print("\n例:")
    print("  python file_utils.py list")
    print("  python file_utils.py list .py")
    print("  python file_utils.py info README.md")
    print("  python file_utils.py count")


if __name__ == "__main__":
    main()

