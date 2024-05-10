"""バーが100%まで動くやつ"""
import time
import shutil


def indicator(rate, length=100):
    if rate == 100:
        print(f'\r[{"=" * length}] 100%')
        return

    coefficient = length / 100
    progress = int(rate * coefficient)
    print(f'\r[{"=" * progress}{" " * (length - progress)}] {rate}%', end='')


def process(length=100):
    for i in range(101):
        indicator(i, length)
        time.sleep(0.1)
    print('\nComplete!')

# デフォルト
process()

# 短め
process(10)

# ターミナルの幅に合わせる
process(shutil.get_terminal_size().columns - 10)
