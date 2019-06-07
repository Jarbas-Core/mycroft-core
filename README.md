# Jarbas Core

Remixes of [Mycroft-core](https://github.com/MycroftAI/mycroft-core)


## Remixes

* [jarbasCore_base](https://github.com/Jarbas-Core/mycroft-core/tree/jarbasCore_base) - reference fork with all stable new features!
* [jarbasCore_private](https://github.com/Jarbas-Core/mycroft-core/tree/jarbasCore_private) - mycroft-core, but with bundled personal backend
* [jarbasCore_offline](https://github.com/Jarbas-Core/mycroft-core/tree/jarbasCore_offline) - mycroft-core, but without backend and on-device STT

## Feature Store

here are branches / PRs of individual features

* [feat/pocketsphinxSTT](https://github.com/Jarbas-Core/mycroft-core/pull/1) - adds pocketsphinx as an offline STT option
* [feat/free_google](https://github.com/Jarbas-Core/mycroft-core/pull/2) - adds support for free Google STT

## Repo Structure

branch naming conventions and meanings

* dev - last syncronization with mycroft-core, unmodified
* feat/XXX - new mycroft-core feature, PR can be made against mycroft, periodically rebased against dev
* bug/XXX - mycroft-core bugfix, PR can be made against mycroft, periodically rebased against dev
* jarbasCore_XXX - XXX is descriptive of changes applied, description and link in main branch README.md
* feat_jarbas/XXX - new jarbas-core feature, non mycroft-compatible
* bug_jarbas/XXX - jarbas-core bugfix, non mycroft-compatible
