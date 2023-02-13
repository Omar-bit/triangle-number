def triangleOrNot(ch):
    s=sum([ord(i)-64 for i in ch])
    return sum(range(1,s+1))==(s*(s+1)/2)

print(triangleOrNot("AB"))