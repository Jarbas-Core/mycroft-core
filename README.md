# Jarbas Core - Server

Fork of mycroft-core, made fully independent of home backend and optimized for privacy

All audio input/output was removed from this version, meant to run on servers/text mode only

Assuming this runs on a server and is directed at multiple users the 
following skills are blacklisted
        
        "blacklisted_skills": [
            "mycroft-volume.mycroftai", 
            "mycroft-alarm.mycroftai",
            "mycroft-npr-news.mycroftai", 
            "mycroft-timer.mycroftai",
            "mycroft-singing.mycroftai", 
            "mycroft-audio-record.mycroftai",
            "mycroft-playback-control.mycroftai", 
            "mycroft-naptime.mycroftai", 
            "mycroft-reminder.mycroftai"
            ]
    
## Features

here are branches / PRs of individual features

* [feat/optional_backend](https://github.com/Jarbas-Core/mycroft-core/pull/3) - removes the need for a home backend
* [feat/private_mail](https://github.com/Jarbas-Core/mycroft-core/pull/6) - send email from your account to any recipient, and not from backend
* [feat/converse_timeout_event](https://github.com/Jarbas-Core/mycroft-core/pull/4) - new event to allow skills to know when they are no longer active (converse method for continuous dialog)
* [feat/message_targetting](https://github.com/Jarbas-Core/mycroft-core/pull/5) - allow bus messages to be targetted at specific components
* [feat/flexible_lang_dir](https://github.com/Jarbas-Core/mycroft-core/pull/7) - fallback to same language dialects if main is missing, "en-uk" -> "en-us"
* [feat/fallback_order_override](https://github.com/Jarbas-Core/mycroft-core/pull/11) - Override fallback skill execution order in configuration


## Repo Structure

branch naming conventions and meanings

* dev - last syncronization with mycroft-core, unmodified
* feat/XXX - new mycroft-core feature, PR can be made against mycroft, periodically rebased against dev
* bug/XXX - mycroft-core bugfix, PR can be made against mycroft, periodically rebased against dev
* jarbasCore_XXX - XXX is descriptive of changes applied, description and link in main branch README.md
* feat_jarbas/XXX - new jarbas-core feature, non mycroft-compatible
* bug_jarbas/XXX - jarbas-core bugfix, non mycroft-compatible
