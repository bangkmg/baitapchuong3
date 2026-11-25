import math
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def la_so_chinh_phuong(n):
    if n < 1:
        return False
    can_bac_hai = math.isqrt(n)
    return can_bac_hai * can_bac_hai == n
def tong_chu_so(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
def main():
    while True:
        try:
            n = int(input("Nhập vào một số nguyên dương n: "))
            if n > 0:
                break
            else:
                print("Vui lòng nhập số lớn hơn 0!")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên!")
    print(f"\n--- KẾT QUẢ PHÂN TÍCH SỐ {n} ---")
    if la_so_nguyen_to(n):
        print(f"- {n} LÀ số nguyên tố.")
    else:
        print(f"- {n} KHÔNG phải là số nguyên tố.")
    if la_so_chinh_phuong(n):
        print(f"- {n} LÀ số chính phương.")
    else:
        print(f"- {n} KHÔNG phải là số chính phương.")
    print(f"- Tổng các chữ số của {n} là: {tong_chu_so(n)}")
if __name__ == "__main__":
    main()