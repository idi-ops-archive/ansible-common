import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_rsyslog_service(Service):
    s = Service('rsyslog')

    assert s.is_enabled
    assert s.is_running


def test_chronyd_service(Service):
    s = Service('chronyd')

    assert s.is_enabled
    assert s.is_running


def test_sudoers(File):
    f = File('/etc/sudoers')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o440


def test_user(User):
    u = User('testuser')

    assert u.exists


# Workaround for testinfra/issues/187
def test_root_password(Command):
    assert Command("sudo getent shadow root").stdout.split(':')[1] == '!!'


def test_group(Group):
    g = Group('testgroup')

    assert g.exists


def test_resolv(File):
    f = File('/etc/resolv.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
