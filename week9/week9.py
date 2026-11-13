def is_odd(n):
    if  n % 2 == 0 :
        return False
    else:
        return True

print(is_odd(5))
print(is_odd(4))


def isleap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(isleap(2024))




def print_triangle(num):
    total = 0
    for i in range(1, num + 1):
        total += i
        print(i , total)

print_triangle(5)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(10))

def reverse (s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse("hello world"))


def reverse_slice (s):
    return s[::-1]

print(reverse_slice("hello world"))



def remove_all (sub , s):
    return s.replace(sub, "")

def remove (sub , s):
    return s.replace(sub, "*")



print(remove_all("an" , "banana"))
print(remove("l" , "hello world"))


def substitute (message , key ):
    alphabet = "abcdefghigklmnopqrstuvwxyz"
    result = ""
    for ch in message:
        index = alphabet.find(ch.lower())
        if index == -1:
            result = ch + result
        elif ch.isupper():
            result = key[index].upper() + result
        else :
            result = key[index].lower() + result

    return result

key = "zyxwvutsrqponmlkgihgfedcbaabc"
print(len(key))

print(substitute("Hello World" , key ))




def remove_dups(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

print(remove_dups("anne"))
print(remove_dups("hello world"))