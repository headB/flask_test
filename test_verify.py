from PIL import Image,ImageFont,ImageDraw,ImageFile
##需要导入随机产生的字符串
import random

def generate_verify():
    chars = 'qwertyupQWERTYUPasdfghjkASDFGHJKzxcvbnmZXCVBNM23456789'

    from io import BytesIO
    ##设置背景的长宽
    width = 130
    height = 50

    ##先生成背景
    bg = Image.new('RGB',(width,height),"white")

    ##设置字体
    font = ImageFont.truetype('FreeSans',40)

    ##其实先查看一下自己能否生成背景先。其他先暂停不做。！
    ##创建draw对象
    draw = ImageDraw.Draw(bg)

    str1 = ''

    ##输出每一个字
    for x in range(5):
        text = random.choice(chars)
        str1 += text
        draw.text
        draw.text((5+random.randint(4,7)+20*x,5+random.randint(3,7)), text=text, fill='black',font=font )




    B1 = BytesIO()
    response_bg = bg.save(B1,'jpeg')



    return B1.getvalue()