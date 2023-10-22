import uvicorn
from fastapi import (FastAPI)

main = FastAPI()


@main.get(path="/")
def submit(console: list[float] | list[int] | list[str] | None = None) -> None:
    ...


if __name__ == '__main__':
    uvicorn.run(
        app=main,
        host="127.0.0.1",
        port=16669
    )
