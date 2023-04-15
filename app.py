import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
@app.route('/predict')
def home():
  return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
  input_features = [float(x) for x in request.form.values()]
  features_value = [np.array(input_features)]

  features_name = ['radius_mean', 'texture_mean', 'area_mean',
       'concavity_mean', 'concave points_mean', 'texture_worst',
       'perimeter_worst', 'concave points_worst']

  df = pd.DataFrame(features_value, columns=features_name)
  output = model.predict(df)

  if output == 1:
      res_val = "Breast cancer"
  else:
      res_val = "no Breast cancer"


  return render_template('index.html', pred='Patient has {}'.format(res_val))

if __name__ == "__main__":
  app.run()


