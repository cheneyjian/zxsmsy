import qrcode
import os

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

# 创建文件夹
folder_name = "qrcode"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 遍历前120个文本并生成二维码
for text in symbol_texts[:120]:
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 将文本添加到二维码中
    qr.add_data(text)
    qr.make(fit=True)

    # 创建图像对象
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存二维码图像
    img.save(os.path.join(folder_name, f"qrcode_{text}.png"))

    print(f"文本 '{text}' 已转换成二维码并保存在 {folder_name} 文件夹中。")
