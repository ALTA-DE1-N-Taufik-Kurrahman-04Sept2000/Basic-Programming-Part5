#  O(n^2)
def muncul_sekali(angka):
    unique_digits = []

    for i in range(len(angka)):
        is_unique = True
        for j in range(len(angka)):
            if i != j and angka[i] == angka[j]:
                is_unique = False
                break
        if is_unique:
            unique_digits.append(int(angka[i]))

    return unique_digits

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]