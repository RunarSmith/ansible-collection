baseline
========

This role configure the system basics :

- apt mirrors
- locale (keyboard, timezone)
- update localedb

Requirements
------------

Nothing special.

Role Variables
--------------

Variables are set by default, but can be overloaded to fit your needs :

- locale_system: example `fr_FR.UTF-8`
- locale_system_language: example: `fr_FR`
- locale_keyboard_layout: example: `fr`
- locale_timezone: the timezone to use. ex : `Europe/Paris`

By defaut, this is set for french.

Dependencies
------------

Nothing special.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.baseline

License
-------



Author Information
------------------

