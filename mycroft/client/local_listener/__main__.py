from mycroft.util.signal import create_signal
from mycroft.util import create_daemon, wait_for_exit_signal
from mycroft.util.lang import get_primary_lang_code
from mycroft.util.log import LOG
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

    # TODO read from mycroft config
    CONFIG = {
        "listener": {
            "default_volume": 150,
            "default_aggressiveness": 2,
            "default_model_dir": '/opt/kaldi/model/kaldi-generic-{lang}-tdnn_250',
            "default_acoustic_scale": 1.0,
            "default_beam": 7.0,
            "default_frame_subsampling_factor": 3,
        },
        "hotwords": {
            "time": {
                "transcriptions": ["what time is it"],
                "sound": None,
                "intent": "current time",
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

    kaldi = KaldiWWSpotter(lang=get_primary_lang_code(), config=CONFIG)
    bus = WebsocketClient()  # Mycroft messagebus, see mycroft.messagebus

    kaldi.on("hotword", handle_hotword)


    def print_hotword(event):
        LOG.info("HOTWORD: " + event)


    def print_utterance(event):
        LOG.debug("LIVE TRANSCRIPTION: " + event)


    kaldi.on("transcription", print_utterance)
    kaldi.on("hotword", print_hotword)

    create_daemon(bus.run_forever)
    create_daemon(kaldi.run)

    wait_for_exit_signal()

