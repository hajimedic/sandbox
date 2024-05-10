"""くるくるするやつ"""
import time

indicators = ['\\', '|', '/', '-']
for i in range(10):
    print(indicators[i % 4], end='\r', flush=True)
    time.sleep(0.5)

print('done!')
