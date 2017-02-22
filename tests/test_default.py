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


def test_user(User, Sudo):
    with Sudo():
        u = User('testuser')

        assert u.exists
        assert u.password == '!!'
        assert u.group == 'testgroup'


def test_root_password(User, Sudo):
    with Sudo():
        u = User('root')

        assert u.exists
        assert u.password == '!!'


def test_group(Group):
    g = Group('testgroup')

    assert g.exists


def test_resolv(File):
    f = File('/etc/resolv.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
