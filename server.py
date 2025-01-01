from flask import Flask, request
from vosk import Model, KaldiRecognizer
import wave

app = Flask(__name__)
model = Model("model")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.data
    rec = KaldiRecognizer(model, 16000)

    if rec.AcceptWaveform(audio):
        return rec.Result()
    return rec.PartialResult()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


