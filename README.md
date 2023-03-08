ansible-cssr-ocp
=========

Deploy CSSR instance into OpenShift.

Variables
--------------

The following variables can be overriden.

| Name                    | Default value         |                                                                                  |
|-------------------------|-----------------------|----------------------------------------------------------------------------------|
| cssr_namespace          |                       | OpenShift namespace                                                              |
| cssr_network_attachments|                       | Network attachments to be created in the OpenShift namespace                     |
| cssr_name               |                       | Name of the CSSR Node                                                            |
| cssr_routername         |                       | Name of CSSR Router                                                              |
| cssr_conductor_ip       |                       | CSSR Conductor IP or hostname                                                    |
| cssr_conductor_user     |                       | CSSR Conductor Username                                                          |
| cssr_conductor_password |                       | CSSR Conductor Password                                                          |


Example variables
--------------

Example variables can be found in the example_vars.yml file.

Running the playbook from the CLI
--------------

ansible-playbook -e @example_vars.yml site.yml

Running the playbooks from automation controller
--------------

Individual playbooks can be built into a workflow in automation controller. 

![](static/workflow.png)

Custom credential in automation controller.
--------------

The conductor credentials can be added into automation controller as a customer credential:

To create the custom credential, use the following structure within AAP.

Input Configuration:

```bash
fields:
  - id: cssr_conductor_ip
    type: string
    label: cssr conductor hostname or ip
  - id: cssr_conductor_user
    type: string
    label: cssr conductor username
  - id: cssr_conductor_password
    type: string
    label: cssr conductor password
    secret: true
```

Injector Configuration:

```bash
extra_vars:
  cssr_conductor_ip: '{{ cssr_conductor_ip }}'
  cssr_conductor_user: '{{ cssr_conductor_user }}'
  cssr_conductor_password: '{{ cssr_conductor_password }}'
```


