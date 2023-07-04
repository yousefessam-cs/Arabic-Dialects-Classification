import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from Preprocess import Preprocess

preprocessor = Preprocess()

class ModelPredict():
    def __init__(self) -> None:
        # class labels
        self.label_dict = {0: 'EG', 1: 'LB', 2: 'LY', 3: 'MA', 4: 'SD'}

        # load trained model and tokenizer
        try:
            self.model = load_model('model.h5')
            with open('tokenizer.pickle', 'rb') as f:
                self.tokenizer = pickle.load(f)
        except:
            self.model = None

    def predict(self, texts: [str]):
        res = []
        if self.model:
            # apply preprocess
            txt = []
            for sentence in texts:
                txt.append(preprocessor.remove_all(sentence))

            # convert to numpy array
            text = np.array(txt)

            # Text tokenization
            trunc_type = 'post'
            padding_type = 'post'
            MAX_SEQUENCE_LENGTH = 250

            text = self.tokenizer.texts_to_sequences(text)
            text = pad_sequences(text, maxlen=MAX_SEQUENCE_LENGTH, padding=padding_type, truncating=trunc_type)

            prediction = self.model.predict(text)

            label = prediction.argmax(axis=1)
            for i, l in enumerate(label):
                res.append(f'Sentence after preprocessing: "{txt[i]}", Prediction: {self.label_dict[int(l)]}')
        else:
            raise Exception("No Trained model was found.")
        return res
