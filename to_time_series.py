


def read():
    file_path = "\\DataRacing2022_datasets\\train.csv"
    f = open(file_path, 'r')
    l = 0
    for line in f:
        print(line)
        l += 1
        if l == 10:
            break
    f.close()
    return v

def main():
    v = read()
    return


if __name__ == "__main__":
    main()