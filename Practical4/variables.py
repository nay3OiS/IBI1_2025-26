a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if d>e:
    print("Population growth is accelerating")
elif d<e:
    print("Population growth is decelerating")
else:
    print("Population growth is constant")