from PIL import Image
import argparse
# asiic_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
asiic_char = list("$@@%%##**oo??--__++~~<<>>;;::.,\"\"^^``'.. ")
# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ' '
    length = len(asiic_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return asiic_char[int(gray/unit)]

# 命令行输入参数处理
parser = argparse.ArgumentParser()
# 输入文件
parser.add_argument('file')
# 输出文件
parser.add_argument('-o','--output')
# 输出字符画
parser.add_argument('--width',type=int,default=80)
parser.add_argument('--height', type = int, default = 80) #输出字符画

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)