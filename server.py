import socket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from pycorrector import Corrector
from loguru import logger

app = FastAPI()
model = Corrector()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputParam(BaseModel):
    text: str = None

@app.post("/TextCorrection/text")
def text_correction(feed: InputParam):
    try:
        assert type(feed.text) is str
        assert len(feed.text) > 0
    except Exception as e:
        logger.info('Parameter error, {}', e)
        return {"code": 400,
                "message": "参数类型异常"}
    try:
        corrected_sent, detail = model.correct(feed.text)
        logger.info('Call interface, input is {}', feed.text)
        return {"code": 200,
                "corrected_text": corrected_sent,
                "detail": detail,
                "message": "请求成功"}
    except Exception as e:
        logger.info('Call interface, input is {}, Error is {}', feed.text, e)
        return {"code": 500, "message": "请求失败"}

if __name__ == '__main__':
    def get_host_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            ip_ = s.getsockname()[0]
        finally:
            s.close()
        return ip_

    ip = get_host_ip()
    uvicorn.run("service:app", host=ip, port=8010, reload=True)