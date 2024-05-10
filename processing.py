"""バーが100%まで動くやつ"""
import time
import shutil


def loading(length=100):
    coefficient = length / 100
    for i in range(101):
        progress = int(i * coefficient)
        print(f'\r[{"=" * progress}{" " * (length - progress)}] {i}%', end='')
        time.sleep(0.1)
    print('\nComplete!')

# デフォルト
loading()

# 短め
loading(10)

# ターミナルの幅に合わせる
loading(shutil.get_terminal_size().columns - 10)
