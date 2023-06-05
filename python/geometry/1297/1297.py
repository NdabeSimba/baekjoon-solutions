cross, width, length = map(int,input().split())
ratio = cross / (width**2 + length**2)**0.5
print(int(width*ratio),int(length*ratio))