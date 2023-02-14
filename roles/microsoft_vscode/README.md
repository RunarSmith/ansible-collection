microsoft_vscode
================

Deploy Visual Studio Code on the host, and install a few extensions.

Note: The Microsoft repository is added during the instalation, but removed after the installation, since I noticed some incompatibilities with the base plateform when installing/upgrade some other applications/packages.

Requirements
------------

nothing special.

Role Variables
--------------

A default list of extensions to install can be configured :

```yaml
vscode_extensions:
  - ms-python.python
  - ms-vscode.powershell
  - redhat.ansible
  - ms-ceintl.vscode-language-pack-fr
  - silofy.hackthebox
```

Dependencies
------------

Nothing special

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.microsoft_vscode

License
-------


Author Information
------------------

