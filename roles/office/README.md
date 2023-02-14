office
======

Install packages, and remove useless packages.

Requirements
------------

Nothing special.

Role Variables
--------------

Check the `default/main.yml` for the list of installed packages, and remove ones.

Packages can be installed from apt repository, or from an URL (ex: deb package released on github).

This install :
- remmina : for RDP
- flameshot : for screenshot taking with annotations
- obsidian : for notes

This remove:
- office packages
- games packages
- some other fat useless packages

```yaml
apt_deb_packages:
  - remmina

apt_deb_url:
  - https://github.com/flameshot-org/flameshot/releases/download/v12.1.0/flameshot-12.1.0-1.debian-11.amd64.deb
  - https://github.com/obsidianmd/obsidian-releases/releases/download/v1.0.3/obsidian_1.0.3_amd64.deb

apt_deb_remove:
   - anonsurf*
   - brasero*
   - geany*
   - gimp*
   - libreoffice*
```

Dependencies
------------

Nothing special

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.office

License
-------


Author Information
------------------
