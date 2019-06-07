# Jarbas Core - Private

Fork of mycroft-core, made fully independent of home backend and optimized for privacy

## Features

here are branches / PRs of individual features

* [feat/pocketsphinxSTT](https://github.com/Jarbas-Core/mycroft-core/pull/1) - adds pocketsphinx as an offline STT option
* [feat/free_google](https://github.com/Jarbas-Core/mycroft-core/pull/2) - adds support for free Google STT, key is shared by many users
* [feat/optional_backend](https://github.com/Jarbas-Core/mycroft-core/pull/3) - removes the need for a home backend
* [feat/private_mail](https://github.com/Jarbas-Core/mycroft-core/pull/6) - send email from your account to any recipient, and not from backend

## Repo Structure

branch naming conventions and meanings

* dev - last syncronization with mycroft-core, unmodified
* feat/XXX - new mycroft-core feature, PR can be made against mycroft, periodically rebased against dev
* bug/XXX - mycroft-core bugfix, PR can be made against mycroft, periodically rebased against dev
* jarbasCore_XXX - XXX is descriptive of changes applied, description and link in main branch README.md
* feat_jarbas/XXX - new jarbas-core feature, non mycroft-compatible
* bug_jarbas/XXX - jarbas-core bugfix, non mycroft-compatible
