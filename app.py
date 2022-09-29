import os

from app import create_app


app = create_app('development')


if __name__ == '__main__':
    # print(os.getenv('name'))
    # print(os.getenv('password'))
    # print(os.getenv('server'))
    # print(os.getenv('port'), type(os.getenv('port')))
    # print(os.getenv('database'))

    app.run()


