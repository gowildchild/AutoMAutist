# Changelog

## 0.0.25

- Rewrote entire addon for AutoMAutist:REST for the newest HASSIO
- Bitmask structure has been added

## 0.0.26

- Bug-fixes

## 0.0.35

- Getting it to work

## 0.0.36

- Adding Gunicorn to add a few workers

## 0.0.37

- Gunicorn chdir /app

## 0.0.38

- Dashboard Redirection Change

## 0.0.39

- Trying to get this faster to load with preloading

## 0.0.40

- Fixed deprecated items
- More dynamic fields for settings
- Removed SYS_ADMIN
- fixed map
- Added CSRF_TRUSTED_ORIGINS as an option
- Auto-generating keys, to nudge towards the right thing in security!

## 0.1.02

- Build was hanging!

## 0.1.03

- Added homeassistant_config safely
- removed secret_key and encryption_salt from UI defaults
- Marked OIDC fields as optional for now

## 0.1.04-alpha

- updated private config

## 0.1.06-alpha

- updated templates with relative URLs
- removed cloud script loading

## 0.1.07-alpha

- lets not hardcode django url's like it should be will we ..

## 0.1.08-alpha

- changed IntegerFields to BigIntegerFields for future changes

## 0.1.08-beta

- added mood selector for cards

## 0.1.08-charlie

- customizing the cards

## 0.1.08-delta

- static fixes for bootstrap and adding dynamic settings

## 0.1.08-echo

- cards have to be more compact, language support and text size support

## 0.1.08-foxtrot

- cards should work in stand-alone mode AND with Home Assistent ingress

## 0.1.08-golf

- ingres was not loading bootstrap

## 0.1.09-alpha

- version bump

## 0.1.10-alpha

- inject ingress when installed as Home Assistant Addon

## 0.1.11-public

- First Public Release : Skeleton of how the server is going to look

## 0.1.11-milestone

- The first milestone of porting 4 REST servers into one with all the functions combined.
