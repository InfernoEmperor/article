from orm.redis import OperateRedis
from orm.record import Record
from .styleMove import GenerateResult
import uuid
import time
from PIL import Image

def Deal(email, mainPic, assistPic):
    result = PicDeal(mainPic, assistPic)  #返回一个生成的ID
    OperateRedis().Set(email, result)
    Record().SetRecord(email, mainPic, assistPic, result)

def PicDeal(mainPic, assistPic):
    img = Image.open(mainPic)
    height = img.size[0]
    width = img.size[1]
    img = Image.open(assistPic)
    if img.size[0] != height or img.size[1] != width:
        #报错
        return "请确保图片格式一致"
    resultPic = GenerateResult(mainPic, assistPic, height, width)
    resultName = uuid.uuid3(uuid.NAMESPACE_OID, str(int(time.time()))) + ".jpg"
    with open('./static/upfile/'+ resultName,'wb') as f:
        f.write(resultPic)
    return resultName