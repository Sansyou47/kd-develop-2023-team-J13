from flask import Blueprint

app = Blueprint('func', __name__)

@app.route('/test')
def blueprint_test():
    return 'これはBlueprintによるファイル分割テストです。表示されていれば成功です。'