# Jarbas Core - Base

jarbas-core base is a fork of mycroft-core, this is my reference implementation that showcases the most stable new features

all branches in this repo named ```feat_jarbas/XXX``` or ```bug_jarbas/XXX``` are periodically rebased against this branch

this might not be the right choice for you, check the Remixes section on the main branch for alternatives.

## Features

I'm trying to make this a bit like a feature store, link to individual PRs

* [link to feature PR]() - feature descrition

## Repo Structure

branch naming conventions and meanings

* dev - last syncronization with mycroft-core, unmodified
* feat/XXX - new mycroft-core feature, PR can be made against mycroft, periodically rebased against dev
* bug/XXX - mycroft-core bugfix, PR can be made against mycroft, periodically rebased against dev
* jarbasCore_XXX - XXX is descriptive of changes applied, description and link in main branch README.md
* feat_jarbas/XXX - new jarbas-core feature, non mycroft-compatible
* bug_jarbas/XXX - jarbas-core bugfix, non mycroft-compatible
