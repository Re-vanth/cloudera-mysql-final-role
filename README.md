# ICDS Data Lake Infrastructure Automation

These ansible playbooks that installs the tools required for ICDS Data Lake on RHEL/CentOS.
- [Cluster Topology](#cluster-topology)
- [Setting up Ansible Control Node](#setting-up-ansible-control-node)
- [Cloudera](#cloudera)
- [Ansible Vault](#ansible-vault)

We have provided all the details about roles that need to be used as part of the [README](https://github.com/FissionHQ/dimagi-datawarehouse/blob/master/ansible-data-lake/roles/README.md) of roles.

# Cluster Topology

We will have following Big Data eco system tools setup on the cluster using Cloudera Manager.

* Setup Cloudera Manager and Agents
* Setup HDFS and YARN
* Configure High Availability
* Setup Hive
* Setup Spark and Kafka
* Setup Hue

Click [here](https://docs.google.com/spreadsheets/d/10LysOo4hEgwe748WAVfAt2psQRqGFrbSkGUPNV4J7Rw) for the topology diagram used for setting up test environment.

# Setting up Ansible Control Node

* Setup an [Ansible Control Node](http://docs.ansible.com/ansible/intro_installation.html) where we can run the ansible and ansible playbooks. Control Node can be any machine with a Debian, Redhat or macOS operating system with python installed.

* Modify Ansible configuration file (optional):
If you want to customize any default properties of ansible, you can change then in ansible.cfg file located in /etc/ansible/ by defualt.

```ini
$ vi ~/.ansible.cfg

[Roles Path]
# additional paths to search for roles in, colon separated
#roles_path    = /etc/ansible/roles
```

* Create [Inventory](http://docs.ansible.com/ansible/intro_inventory.html) file with list of managed nodes <br />
  * Default Inventory file location - /etc/ansible/hosts. We can specify a inventory at a different location using -i option in the command line. Sample Inventory file required for this is available as part of the repository. <br />
  * Ansible communicates with the hosts defined in the inventory over SSH by assuming ssh key authentiation by default, so your public SSH key should exist in authorized_keys on those hosts. The defined user will need sudo privileges to install the required packages.

# Ansible Playbook
Here are the steps to run the playbook which will install all the pre-requisites and also setup Cloudera Manager and Agents.

* Create hosts file as per the topology diagram.
* Here is the [sample hosts file](https://github.com/FissionHQ/dimagi-datawarehouse/blob/master/ansible-data-lake/hosts) used for test environment.
* Update [all.yml in group_vars](https://github.com/FissionHQ/dimagi-datawarehouse/blob/master/ansible-data-lake/group_vars/all.yml) to reflect correct versions and server names based up on the environment we are going to deploy.
* Run the playbook using below command.
```ini
ansible-playbook -i hosts site.yml
```

# Cloudera
There are three roles to deploy Cloudera distribtion. The goal of these roles is to install setup cloudera repo, install cloudera manager and agents based on the defined inventory.
- Works with RHEL/CentOS 6 or 7 x86_64.

Click [here](https://github.com/FissionHQ/dimagi-datawarehouse/tree/master/ansible-data-lake/roles#cmrepo-cmserver-and-cmagent) for the details to understand more about setting up CM and CDH before adding services.

# Ansible Vault
We will use ansible vault to encrypt senstive data like passwords in the variables file. Get ansible vault documentation from [here](https://docs.ansible.com/ansible/latest/user_guide/vault.html). To test any ansible role, go to the corresponding role folder in roles.

Using ansible vault with interactive prompt
```ini
ansible-playbook --ask-vault-pass site.yml
```
Using ansible vault with a password file
```ini
ansible-playbook --vault-password-file /path/to/my/vault-password-file site.yml
```
Using ansible vault from an Environment variable either the password or the password file using the below.
```ini
export VAULT_PASSWORD=my_vault_password
or
export ANSIBLE_VAULT_PASSWORD_FILE=/path/to/my/vault-password-file
```

We will be using ansible-vault encrypt_string command to encrypt the password string and assign to a variable which can be used in YAML files.
```ini
ansible-vault encrypt_string admin --name 'mysql_password'
```


We can use the output of above which is encryting the password 'admin' and assign to a variable 'mysql_password'.
```ini
mysql_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          38316636326162613739616261333431336565653836303136393764636262663766616432646635
          31393536353835336265656358454545683563653535965365353561386263396362386131356238
          65653733316134666131383533323436376562353339376165333436626663666231633665663734
          6237646566343639620a356261623638323961343531343738633066303561393933636133663233
          6330
```



