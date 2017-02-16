Ansible 'common' role
=====================

Applies basic configuration settings

**Important**: Only tested with servers and VMs running on IDRC's datacenter.


Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

These options are useful to ensure root logins are not permitted to certain servers (even if an attacker gains access to the console or can bypass SSH restrictions somehow -- physical access to hard disk renders these useless though):

    common_unset_root_password: yes
    common_remove_root_authorized_keys: yes

By default, this role will use TCP connections to remote syslog servers. 

    common_syslog_port: 601

List of remote syslog servers. The rsyslog behavior is tweaked to ensure messages are sent to ALL servers simultaneously:

    common_syslog_servers: []

In case it's necessary to ensure certain RPM packages are installed across all servers (and they can't be added to the VM template or Cobbler/Kickstart configuration for any reason), list them here:

    common_packages: []

# NTP servers used by chrony (should be configured with the closest servers):

    common_ntp_servers:
      - 0.pool.ntp.org
      - 1.pool.ntp.org
      - 2.pool.ntp.org
      - 3.pool.ntp.org

# Default DNS resolvers to be used in /etc/resolv.conf

    common_nameservers:
      - 8.8.8.8
      - 8.8.4.4

# You may want to tweak how names are resolved (see resolv.conf(5) man page for more details)

    common_resolvconf_options: single-request-reopen


Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - common


Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and SELinux, only a Vagrant provider is configured at the moment.


License
-------

MIT
