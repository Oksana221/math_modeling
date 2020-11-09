a=[3,3,5,4,3,2]
def sr(num):
    return float(sum(num)) / max(len(num), 1)
print(sr(a))