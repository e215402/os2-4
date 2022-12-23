import os
import fnmatch

sarchDirPath_input = input('input directory path: ')
sarchDirPath = os.path.expanduser(sarchDirPath_input)

def wc(file_path):
    with open(file_path, 'r', encoding='iso-8859-1') as f:
        lines = 0
        words = 0
        bytes = 0
        for line in f:
            lines += 1
            words += len(line.split())
            bytes += len(line)
    return (lines, words, bytes)

def find(extension):
    pattern = f'*{extension}'
    for root,dir,files in os.walk(sarchDirPath):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                file_path = os.path.join(root, file)
                lines, words, bytes = wc(file_path)
                print(f'{lines} {words} {bytes} {file_path}')

extensions_input = input('Extension you want to search for: ')
extensions = extensions_input.split()

for extension in extensions:
    find(extension)





# import os
# import fnmatch

# # 探索したいディレクトリのパス
# sarchDirPath_input = input('input directory path: ')
# sarchDirPath = os.path.expanduser(sarchDirPath_input)

# # wcの働きをする関数
# def wc(file_path):
#     # ファイルを開く
#     with open(file_path, 'r', encoding='iso-8859-1') as f:
#         # 行数、単語数、バイト数をカウントする
#         lines = 0
#         words = 0
#         bytes = 0
#         for line in f:
#             lines += 1
#             words += len(line.split())
#             bytes += len(line)
#     # 結果をタプルで返す
#     return (lines, words, bytes)

# # findの働きをする関数
# def find(extension):
#     # 拡張子を含むファイル名のパターンを作成
#     pattern = f'*{extension}'
#     # sarchDirPath直下のディレクトリ内のファイルを検索
#     for root,files in os.walk(sarchDirPath):
#         # ファイル名がパターンにマッチするファイルをカウント
#         for file in files:
#             if fnmatch.fnmatch(file, pattern):
#                 # ファイルのフルパスを取得
#                 file_path = os.path.join(root, file)
#                 # 行数,単語数,バイト数をカウント
#                 lines, words, bytes = wc(file_path)
#                 # 結果を表示
#                 print(f'{lines} {words} {bytes} {file_path}')

# extensions_input = input('Extension you want to search for: ')

# # 入力された文字列を半角スペースで分割し、リストにする
# extensions = extensions_input.split()

# for extension in extensions:
#     find(extension)
