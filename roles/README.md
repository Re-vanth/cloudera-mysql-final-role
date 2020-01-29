# Hadoop Deployment - Ansible Roles

The following ansible roles defined to install and configure the Hadoop Ecosystem stack on RHEL/CentOS.

* [Pre-Requisites](#pre-requisites)
* [Setting up MySQL Database](#setting-up-mysql-database)
* [Setting up krb5_client](#setting-up-krb5_client)
* [Setting up krb5_server](#setting-up-krb5_server)
* [Setting up AirFlow](#setting-up-airflow)

# Pre-Requisites
Run this role to setup the pre-requisites for the cluster using Cloudera Distribution. Here are some of the pre-requisites.

* Make sure JDK 1.8 is setup on all the nodes.
* Disable selinux
* Create necessary users and directories
* Disable OS level firewalls
* Make necessary Kernel level changes such as disabling Swappiness.

We can run the role using the below command.
```ini
ansible-playbook -i hosts site.yml --tags=prereq
```

# Setting up MySQL Database
To install the MySQL database and create the required databases.

We can run the role using the below command.
```ini
ansible-playbook -i hosts site.yml --tags=database
```

# Setting up Cloudera Components

As part of Cloudera Distribution we need to ensure that Cloudera Manager is running on one host and Agent is running on all the nodes.

- cmrepo: We need to download repository file so that we can setup required Cloudera Components. This role will take care of downloading repository file on all the servers.
- cmserver: Install the Cloudera Manager Server on a centralized server. We will also setup all the components related to Management Service on the same node where Cloudera Manager is running. This role will take care of setting up Cloudera Manager.
- cmagent: Install the Cloudera Manager agent on all the hosts. This role will ensure that Cloudera Agent is setup on all the nodes in the cluster.

We can run the roles using the below commands.
```ini
ansible-playbook -i hosts site.yml --tags=cmrepo
ansible-playbook -i hosts site.yml --tags=cmserver
ansible-playbook -i hosts site.yml --tags=cmagent
```




