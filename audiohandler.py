import speech_recognition as sr

class AudioHandler:
    def __init__(self, energy_threshold=3000, pause_threshold=0.5):
        self.r = sr.Recognizer()
        self.r.energy_threshold = energy_threshold # 3000 optimal for my setup
        self.r.pause_threshold = pause_threshold # 0.5 worked for my setup
        self.mic = sr.Microphone()

    def process_speech(self):

        with self.mic as source:
            #self.r.adjust_for_ambient_noise(source, duration=0.3)
            audio = self.r.listen(source)
            speech = self.r.recognize_google(audio)
        return speech

