# -*- coding: utf-8 -*-

def chinese_to_big5_decimal(text: str) -> list[int]:
    """
    輸入一串文字，輸出對應到 Big5 編碼的十進位整數列表
    """
    result = []
    for ch in text:
        try:
            # 用 Python 的 big5 編碼取得 bytes
            b = ch.encode("big5")
        except Exception:
            # 無法 Big5 編碼時標示為 None
            result.append(None)
            continue

        # 2 bytes → 10進位： high*256 + low
        high, low = b[0], b[1]
        dec = high * 256 + low
        result.append(dec)

    return result


if __name__ == "__main__":
    print("輸入中文文字查 Big5 十進制值，輸入 'exit' 結束程式。")
    while True:
        s = input("輸入文字：")
        if s.lower() == "exit":
            print("程式結束。")
            break
        codes = chinese_to_big5_decimal(s)
        print(codes)
