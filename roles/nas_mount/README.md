nas_mount
=========

Mount a CIFS share from a NAS on your LAN.

Requirements
------------

You need a CIFS share :)

Role Variables
--------------

In order to mount a share, you need to provide (no default value) the host name, credential, and paths :

```yaml
mount_nas:
  hostname:     nas-host.lan
  shared:       "ShareName"
  mount_point:  /mnt/where/should/I/mount/it/for/you
  username:     myusername
  password:     MySuperSecretP@ssw0rd
```

Dependencies
------------

Nothing special.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.nas_mount

License
-------

Author Information
------------------
