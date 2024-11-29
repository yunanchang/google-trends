# 計算輸入數字的平方
def calculate_square():
    try:
        # 輸入數字
        num = float(input("請輸入一個數字: "))
        # 計算平方
        square = num ** 2
        print(f"數字 {num} 的平方是 {square}")
    except ValueError:
        print("請輸入有效的數字！")

# 主程式
if __name__ == "__main__":
    calculate_square()
