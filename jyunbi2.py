#sota

# ランレングス符号化の展開
wether = []
with open('../jyunbi2', 'rb') as f:
    count = 0
    tmp_li = []
    while True:
        tmp = f.read(1)
        if not tmp:
            break
        tmp = int.from_bytes(tmp, 'big') #降水量
        tmp_li.append(tmp)
        count += 1

        # 同じ数字が続いたとき
        if count == 3:
            wether.extend([tmp_li[0] for i in range(tmp)])
            tmp_li = []
            count = 0
            continue

        # 違う数字が続いたとき
        if tmp_li[0] != tmp:
            wether.extend([tmp_li[0]])
            tmp_li = [tmp_li[1]]
            count = 1

print("encode : {}".format(wether))        

# 出現数の辞書作成
dic = {}
for tmp in wether:
  if tmp in dic:
    dic[tmp] += 1
  else:
    dic[tmp] = 1
print("dictionary : {}".format(dic))

# ハフマンツリー作成
import heapq as hq

h = []
for tmp in dic.items(): #辞書のkey,valueをタプルで渡す
    hq.heappush(h, [tmp[1], str(tmp[0])])
print(h)

l = len(h) - 1
while True:
    a = hq.heappop(h)
    b = hq.heappop(h)
    if len(a[1]) < len(b[1]):
        a, b = b, a
    hq.heappush(h, [a[0]+b[0], [a[1], b[1]]])
    if len(h) == 1:
        break

hahuman_tree = h[0][1]
print("tree : {}".format(hahuman_tree))

# ハフマン符号化で圧縮
def coding(lst, degistr):
     for i, small_lst in enumerate(lst):
        if type(small_lst) == str:
            hahuman[small_lst] = degistr + str(i)
        elif i == 0:
            coding(small_lst, degistr + "0")
        else:
            coding(small_lst, degistr + "1")

hahuman = {}
coding(hahuman_tree, "")

print("decode : {}".format(hahuman))



