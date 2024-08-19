from werkzeug.serving import run_simple


def func():
    print('get')
    pass


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, func())
