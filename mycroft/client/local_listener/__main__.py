from mycroft.util.signal import create_signal
from mycroft.util import create_daemon, wait_for_exit_signal
from mycroft.messagebus.message import Message
from mycroft.messagebus.client.ws import WebsocketClient
from kaldi_spotter import KaldiWWSpotter
import json

bus = None
kaldi = None


def handle_hotword(event):
    event = json.loads(event)
    data = event["data"]
    if data["intent"] == "listen":
        bus.emit(Message('recognizer_loop:wakeword', data))
        create_signal('startListening')
    else:
        data["utterances"] = [data["utterance"]]
        data.pop["utterance"]
        bus.emit(Message('recognizer_loop:utterance', data))


if __name__ == "__main__":
    global bus, kaldi

    kaldi = KaldiWWSpotter()
    bus = WebsocketClient()  # Mycroft messagebus, see mycroft.messagebus

    kaldi.on("hotword", handle_hotword)

    # TODO read from mycroft config
    CONFIG = {
        "lang": "en",  # "en" or "de" pre-trained models available
        "listener": {
            "default_volume": 150,
            "default_aggressiveness": 2,
            "default_model_dir": '/opt/kaldi/model/kaldi-generic-{lang}-tdnn_250',
            "default_acoustic_scale": 1.0,
            "default_beam": 7.0,
            "default_frame_subsampling_factor": 3,
        },
        "hotwords": {
            # simple commands
            "hello": {
                "transcriptions": ["hello"],
                "sound": None,
                "intent": "greeting",
                "active": True,
                # in - anywhere in utterance
                # start - start of utterance
                # end - end of utterance
                # equal - exact match
                # sensitivity - fuzzy match and score transcription (error tolerant) <- default
                "rule": "start"
            },
            "thank you": {
                "transcriptions": ["thank you"],
                "sound": None,
                "intent": "thank",
                "active": True
            },
            # full sentences
            # CRITERIA
            # - fairly accurate,
            # - important enough to want offline functionality
            # - worth answering even if speech not directed at device
            "lights on": {
                "transcriptions": ["lights on"],
                "sound": None,
                "intent": "turn on lights",
                "active": True,
                "sensitivity": 0.2,
                # if score > 1 - sensitivity -> detection
                # hey computer * a computer == 0.8181818181818182
                # "hey mycroft" * "hey microsoft" == 0.8333333333333334
                "rule": "sensitivity"
            },
            "lights off": {
                "transcriptions": ["lights off"],
                "sound": None,
                "intent": "turn off lights",
                "active": True,
                "rule": "equal"
            },
            "time": {
                "transcriptions": ["what time is it"],
                "sound": None,
                "intent": "current time",
                "active": True,
                "rule": "equal"
            },
            "weather": {
                "transcriptions": ["what's the weather like",
                                   "what's the weather life",
                                   "what is the weather like",
                                   "what is the weather life",
                                   "what the weather like"],
                "sound": None,
                "intent": "weather forecast",
                "active": True,
                "rule": "equal"
            },

            # wake words
            "hey computer": {
                "transcriptions": ["hey computer", "a computer",
                                   "they computer"],
                "sound": None,
                "intent": "listen",
                "active": True
            }
        }
    }


    def print_hotword(event):
        print("HOTWORD:", event)


    def print_utterance(event):
        print("LIVE TRANSCRIPTION:", event)


    kaldi.on("transcription", print_utterance)
    kaldi.on("hotword", print_hotword)

    create_daemon(bus.run_forever)
    create_daemon(kaldi.run)

    wait_for_exit_signal()
