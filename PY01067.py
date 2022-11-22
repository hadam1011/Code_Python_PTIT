import itertools

def main():
    test = int(input())
    for i in range(test):
        n = int(input())
        list = ["1", "2"]
        count = 0
        while True:
            num = list.pop(0)
            if(num.count("2") > len(num) / 2):
                print(num, end=" ")
                count += 1
            if count == n:
                break
            list.append(num + "0")
            list.append(num + "1")
            list.append(num + "2")
        print("")

if __name__ == '__main__':
    main()
