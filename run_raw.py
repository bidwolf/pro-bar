'''
    This is a module that contain the flask server
    author: bidwolf
    date: 2024-02-09
'''
import os
from flask import Flask, request,jsonify
from barcode import Code128
from barcode.writer import ImageWriter
app = Flask(__name__)

@app.route('/create_tag', methods=["POST"])
def create_tag():
    '''
    This is a function that create a tag from a product code
    '''
    body = request.json
    product_code = body.get('product_code')
    tag = Code128(product_code, writer=ImageWriter())
    if not os.path.exists('temp'):
        os.makedirs('temp')
    path_of_tag = 'temp/'+f'{tag}'
    tag.save(path_of_tag)
    return jsonify({"path_of_tag": path_of_tag})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=3000)
