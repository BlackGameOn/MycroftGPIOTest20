from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

class BuzzerControl(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('buzzer_skill.intent')
    def handle_buzzer_skill(self, message):
        self.speak_dialog('buzzer_skill')
        GPIO.output(20,True)
        GPIO.output(21,True)

def create_skill():
    return BuzzerControl()

