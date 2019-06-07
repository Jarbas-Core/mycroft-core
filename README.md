# Jarbas Core -Base

jarbas-core base is a fork of mycroft-core, this is my reference implementation that showcases the most stable new features, made fully independent of home backend and optimized for privacy

## Features

here are branches / PRs of individual features

* [feat/pocketsphinxSTT](https://github.com/Jarbas-Core/mycroft-core/pull/1) - adds pocketsphinx as an offline STT option
* [feat/free_google](https://github.com/Jarbas-Core/mycroft-core/pull/2) - adds support for free Google STT, key is shared by many users
* [feat/optional_backend](https://github.com/Jarbas-Core/mycroft-core/pull/3) - removes the need for a home backend
* [feat/converse_timeout_event](https://github.com/Jarbas-Core/mycroft-core/pull/4) - new event to allow skills to know when they are no longer active (converse method for continuous dialog)
* [feat/message_targetting](https://github.com/Jarbas-Core/mycroft-core/pull/5) - allow bus messages to be targetted at specific components


## Repo Structure

branch naming conventions and meanings

* dev - last syncronization with mycroft-core, unmodified
* feat/XXX - new mycroft-core feature, PR can be made against mycroft, periodically rebased against dev
* bug/XXX - mycroft-core bugfix, PR can be made against mycroft, periodically rebased against dev
* jarbasCore_XXX - XXX is descriptive of changes applied, description and link in main branch README.md
* feat_jarbas/XXX - new jarbas-core feature, non mycroft-compatible
* bug_jarbas/XXX - jarbas-core bugfix, non mycroft-compatible
