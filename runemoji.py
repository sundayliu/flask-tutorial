# -*- coding:utf-8 -*-
from emoji import app
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=True)