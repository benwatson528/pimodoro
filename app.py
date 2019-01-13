from flask import Flask
from RGB import RGB
from Pimodoro import runTimer, clearDisplay
import blinkt

STUDY_TIME = 1
REST_TIME = 1
STUDY_COLOUR = RGB(255, 0, 0)
REST_COLOUR = RGB(0, 255, 0)

app = Flask(__name__)

@app.route('/startTimer', methods=['POST'])
def startTimer():
	runTimer(STUDY_TIME, STUDY_COLOUR)
	runTimer(REST_TIME, REST_COLOUR)
	clearDisplay()

@app.route('/stopTimer', methods=['POST'])
def stopTimer():
	clearDisplay()

if __name__ == '__main__':
    clearDisplay()
    app.run(debug=True, host='0.0.0.0', port=80)
