
from machine_learning.Interface import PicDeal


STYLE_IMAGE = r'I:\毕业设计\testProject\static\img\work3.jpg'
CONTENT_IMAGE = r'I:\毕业设计\testProject\static\img\work1.jpg'

if __name__ == "__main__":
    name = PicDeal(STYLE_IMAGE, CONTENT_IMAGE)
    print(name)

