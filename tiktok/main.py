from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend


upload_video('video.mp4',
            description='this is my description',
            cookies='cookies.txt')

videos = [
    {
        'path': 'video.mp4',
        'description': 'this is my description'
    },
    {
        'path': 'video2.mp4',
        'description': 'this is also my description'
    },
{
        'path': 'video2.mp4',
        'description': 'this is also my description'
    },
{
        'path': 'video2.mp4',
        'description': 'this is also my description'
    },
{
        'path': 'video2.mp4',
        'description': 'this is also my description'
    },{

        'path': 'video2.mp4',
        'description': 'this is also my description'
    },
{
        'path': 'video2.mp4',
        'description': 'this is also my description'
    }
]

auth = AuthBackend(cookies='cookies.txt')
upload_videos(videos=videos, auth=auth)