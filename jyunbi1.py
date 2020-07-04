# sota

import numpy as np
import matplotlib.pyplot as plt

with open('../jyunbi1_fixed.wdy', 'rb') as f:
    signature = f.read(2).decode()
    size ,width, height = [int.from_bytes(f.read(4), 'little') for i in range(3)]
    print(signature, size, width, height)

    img = [[[0]*3]*width]*height
    for h in range(height-1, -1, -1):   #下部から上部へ1⾏ずつ
        for w in range(width):          #左から右に1つずつ
            img[h][w] = list(reversed([int.from_bytes(f.read(1), 'little') for bgr in range(3)]))
    print(img[0][0])

    img = np.array(img).astype(np.uint8)

    plt.imshow(img)
    plt.show()

