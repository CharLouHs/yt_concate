from pipeline.steps.get_video_list import GetVideoList

from settings import API_KEY
from pipeline.pipeline import Pipeline

# import ssl
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs={
        'channel_id': CHANNEL_ID

    }
    steps = [GetVideoList()
             ]
    p=Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
