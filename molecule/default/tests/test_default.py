import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_swift_toolchain(host):
    revision = "4.1-RELEASE"
    assert host.file("/opt/swift").exists
    assert host.file("/opt/swift/toolchain_version").exists
    assert host.file("/opt/swift/toolchain_version").contains(revision)


def test_swift_symlink(host):
    link_path = "/opt/swift-4.1-RELEASE-ubuntu16.04"
    assert host.file(link_path).is_symlink
    assert host.file(link_path).linked_to == "/opt/swift"
