def rev(s):
    res = ""
    for i in range(len(s)-1,-1,-1):
        res += s[i]
    return res

def rev01(s):
    res = ""
    for i in range(0,len(s)):
        res = s[i] + res


if __name__ == "__main__":
    s = "Hello"
    print(rev(s))
    print(rev01(s))