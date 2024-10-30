exegol
======

Deploy and configure exegol. A few resources are added.

Requirements
------------

Ethical hacking knowledge :)

Role Variables
--------------

For the configuration, a few variables are set by default to set-up the path of resources and workspace:

```yaml
exegol:
  my_resources: /opt/exegol/my-resources
  exegol_resources: /opt/exegol/exegol-resources
  workspaces:  "{{ ansible_user_dir }}/exegol_workspaces"
```

Dependencies
------------

Nothing special

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.exegol

License
-------


Author Information
------------------

