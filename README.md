# Ansible Collection - runarsmith.ansible_collection

This is a personal collection of the roles I use to configure my hosts. I mostly use them to configure a virtual host to learn ethical hacking.

## Content

This collection contains roles to perform the configuration.

## Installation

Setup the requirements to pull from the git repository:

requirements.yml :

```yaml
collections:
  - name: community.general

  - name: git@github.com:RunarSmith/ansible-collection.git
    type: git
    version: main
```

download the dependencies with :

```bash
ansible-galaxy collection install -r requirements.yml
```

## Usage

From your playbook, call the roles :

playbool.yml :

```yaml
---
- name: Gather facts
  hosts:  all
  gather_facts: yes

- name:   Setup base
  hosts:  all
  gather_facts: no
  roles:
    - runarsmith.ansible_collection.baseline    
    - runarsmith.ansible_collection.ansible_controler
    - runarsmith.ansible_collection.nas_mount
    - runarsmith.ansible_collection.microsoft_vscode
    - runarsmith.ansible_collection.office
    - runarsmith.ansible_collection.exegol
    - runarsmith.ansible_collection.user_git
```

execute the playbook with something like :

```bash
ansible-playbook --ask-become-pass -i inventory.yml playbook.yml
```