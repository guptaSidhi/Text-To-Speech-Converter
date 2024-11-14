from src.exception import CustomException
from src.logger import logging
from flask import Flask,render_template,request
from flask_cors import CORS, cross_origin
from src.components.text_to_speech import TTSApplication
from src.components.get_accent import get_accent_message,get_accent_tld
import sys
import os 

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
@cross_origin()
def home():
    try:
        accent_list = get_accent_message()
        return render_template('index.html',accent_list = accent_list)
    except Exception as e:
        raise CustomException(e,sys)
    
@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':
            data = request.json['data']
            accent_input = request.json['accent']
            accent = get_accent_tld(accent_input)
            result = TTSApplication().texttospeech(data, accent)
            return {"data": result.decode("utf-8")}
    except Exception as e:
        raise CustomException(e, sys)
        flash('Check your input', e)

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)),host="0.0.0.0")