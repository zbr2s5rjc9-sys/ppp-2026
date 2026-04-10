def f2c(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c

def c2f(temp_c):
    return temp_c * 1.8 + 32

def main():
    print(f2c(56))
    print(c2f(26.67))

if __name__ == "__main__":
    main()
