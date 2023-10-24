"""
LiteWearable AppGallery, Community and Self-signed Platform
"""

# import AppGalleryConnect
import uvicorn
# import config.read
# import config.edit
# import config.management
from fastapi import (FastAPI, Response, status)
from fastapi.responses import *

import config.read

# print(config.read.Config.getdata)


LWACS = FastAPI()


@LWACS.get(path="/")
async def docs_redirect(response=Response):
    response.status_code = status.HTTP_301_MOVED_PERMANENTLY
    url = "/docs"
    return RedirectResponse(url=url)


@LWACS.get(path="/account/create")
async def create_account(UUID: str, response=Response) -> Any:
    """
    用于注册一个新账户，账户管理用于社区而不是用于应用签名，该步骤不能省略
    :param UUID: 设备UUID
    :return: 账号的UID
    """
    conf = config.read.Config().getdata()
    for uid in conf["accounts"]:
        for did in conf["accounts"][uid]["devices"]:
            if conf["accounts"][uid]["devices"][did]["UUID"] == UUID:
                response.statue_code = status.HTTP_301_MOVED_PERMANENTLY
                url = f"/account/get_uid?UUID={UUID}"
                return RedirectResponse(url=url)

if __name__ == '__main__':
    uvicorn.run(
        app=LWACS,
        host="127.0.0.1",
        port=8899
    )
