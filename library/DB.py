import pymysql


class connection(object):
    def __init__(self, request=None, params={}):
        self.conn = None

        try:
            self.conn = pymysql.connect(user='root',
                                         host='127.0.0.1',
                                         db='testDB',
                                         password='1q2w3e4r')

        except Exception as e:
            print(e)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        conn = self.conn
        self.cursor.close()
        conn.commit()
        conn.close()


def request_data(request):
    _data = None

    if request.method == 'GET':
        _data = request.query_params.copy()
    else:
        _data = request.data.copy()

    return _data