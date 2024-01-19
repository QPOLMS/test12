from tiktok_uploader.upload import upload_video

from random import choice

BROWSERS = [
    'chrome',
    'safari',
    'chromium',
    'edge',
    'firefox'
]

#randomly picks a web browser
upload_video(..., browser=choice(BROWSERS))