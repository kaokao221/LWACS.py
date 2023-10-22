# import AppGalleryConnect
import uvicorn
# import config.read
# import config.edit
# import config.management
from fastapi import (FastAPI, Response, Request)
from fastapi.responses import *

# print(config.read.Config.getdata)


main = FastAPI()


@main.get(path="/")
async def root(command_code: str | None = None, response=Response, requests=Request):
    """
    Which is the root application
    :param command_code:
    :param response:
    :param requests:
    :return:
    """
    response.status_code = 301
    response.redirect = "/main/"
    url = "/main"
    return RedirectResponse(url=url)


@main.post(path="/")
async def root(command_code)

if __name__ == '__main__':
    uvicorn.run(
        app=main,
        host="127.0.0.1",
        port=8899
    )
