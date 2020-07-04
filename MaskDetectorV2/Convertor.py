
from tensorflow import lite
from tensorflow.keras.models import load_model

model1 = load_model("a.h5")
converter = lite.TFLiteConverter.from_keras_model(model1) # Your model's name
model = converter.convert()
file = open( 'model.tflite' , 'wb' )
file.write( model )
