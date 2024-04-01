def generate_symbol_text():
    symbol_texts = []
    for d3 in range(0, 3):  # 第三位数字范围为 0 到 2
        for d4 in range(0, 10):  # 第四位数字范围为 0 到 9
            for d5 in range(1, 7):  # 第五位数字范围为 1 到 6
                symbol_text = f"PB0{9}{d3}{d4}{d5}"  # 生成符号文本
                symbol_texts.append(symbol_text)
    return symbol_texts

# 生成符号文本列表
symbol_texts = generate_symbol_text()

# 将打印的结果转换为文本列表
text_list = [str(text) for text in symbol_texts]

# 打印转换后的文本列表的前10个
print(text_list[:120])
