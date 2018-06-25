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
    ##定义非白色背景,RBG
    bg_color = (random.randint(20,100),random.randint(20,100),100)
    bg = Image.new('RGB',(width,height),bg_color)

    ##设置字体
    font = ImageFont.truetype('msyh',40)
    #但是不是什么时候系统都有微软雅黑的，所以，得留一个底线。
    #font = ImageFont.truetype('FreeSans',40)

    ##其实先查看一下自己能否生成背景先。其他先暂停不做。！
    ##创建draw对象
    draw = ImageDraw.Draw(bg)

    #验证码的具体字符串形式
    str1 = ''

    ##输出验证码之前需要先添加噪点
    ##然后这里的说法，就是使用draw。point来做。！
    #fill的话，意思是填充什么内容，你填充噪点，也要指定颜色啊～。
    for x in range(0,100):
        xy = (random.randint(0,130),random.randint(0,50))
        fill = (200,random.randint(100,200),random.randint(200,255))
        draw.point(xy,fill=fill)

    ##输出每一个字
    for x in range(5):
        text = random.choice(chars)
        str1 += text
        #这里第一格参数给定left，top的距离坐标，然后还有内容！。
        #draw.text((0+20*x,30), text=text, fill='black',font=font )
        draw.text((5+random.randint(4,7)+20*x,5+random.randint(3,7)), text=text, fill=(255,random.randint(0,255),random.randint(0,255)),font=font )
    
    #draw.text((0,1),text=str1,fill='black',font=font )

    ##到了这一步，其实还是可以添盐加醋的！。
    ##也算是对draw加深认知
    for x in range(10):
        #线的长度
        #线的宽度
        #坐标
        x1 = random.randint(0,width)
        y1 = random.randint(0,height)
        x2 = random.randint(0,width)
        y2 = random.randint(0,height)
        draw.line(((x1,y1),(x2,y2)),fill="black",width=1)
 

    B1 = BytesIO()
    response_bg = bg.save(B1,'gif')
    #response_bg = bg.save(B1,'jpeg')


    #返回图形，还有utf-8格式的字符串验证码
    return B1.getvalue(),str1