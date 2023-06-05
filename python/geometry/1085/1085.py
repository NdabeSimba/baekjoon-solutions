import sys
input = sys.stdin.readline

x, y, w, h = map(int,input().split())

xcal = w-x
ycal = h-y

if xcal > x:
    xcal = x
if ycal > y:
    ycal = y

print(min(xcal,ycal))