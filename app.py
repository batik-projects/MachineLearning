from Flask import flask
import numpy as np
from tensorflow.keras.models import load_model  
from tensorflow.preprocessing import image
from flask import request, jsonify

app = flask(__name__)
model = load_model('model/11ClassEpoch55.keras')


model.make_predict_function()

classes_name = ['BelumDiketahui',
 'batik-asmat',
 'batik-bali',
 'batik-boraspati',
 'batik-gadjah',
 'batik-kawung',
 'batik-lumbung',
 'batik-megamendung',
 'batik-parang',
 'batik-pekalongan',
 'batik-tifa']

def predict_label(img_path):
  i = image.load_img(img_path, target_size=(224, 224), color_mode='rgb')
  i = image.img_to_array(i)
  i = i / 255
  i = np.expand_dims(i, axis=0)
  p = model.predict(i)
  p = np.argmax(p, axis=1)
  
  return classes_name[p[0]]
  
  
@app.route('/predict', method=['POST', 'GET'])
def predict():
  if request.method == 'POST':
    img = request.files['my_img']
    img_path = f'static/{img.filename}'
    img.save(img_path)
    
    predictions = predict_label(img_path)
    
    print(predictions)
    
  return jsonify({
    'prediction': predictions  
  })
    
    
if __name__ == '__main__':
  app.run(debug=True)