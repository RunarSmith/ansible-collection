user_git
========

Install git client, and configure it with your default username and mail

Requirements
------------


Role Variables
--------------

```yaml
git_user:
  username: "mygitusername"
  email: "my@mail.com"
```

Dependencies
------------

Nothing special

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - runarsmith.ansible_collection.user_git

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
