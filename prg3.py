def compare(s1,s2,n):
    if s1[0:n]==s2[0:n]:
        return True
    else:
        return False
s1 = input("enter first string:")
s2 = input("enter the second string:")
n = int(input("enter number of characters to be compared:"))
print(compare(s1,s2,n))
