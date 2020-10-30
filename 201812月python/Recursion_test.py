def digui(k):
    if k>0:
        result= k+digui(k-1)
        print(result)
    else:
        result = 0
    return result

if __name__ == "__main__":
    digui(7)
    print(__name__)
