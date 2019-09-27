from monitor import find_ip

def test_find_ip():
    assert find_ip("Sep 24 11:18:17 jump-eu-001 sshd[20544]: reverse mapping checking getaddrinfo for 253060.050101.kansai-bb.com [101.50.60.253] failed - POSSIBLE BREAK-IN ATTEMPT!") == "101.50.60.253"
    assert find_ip("Sep 24 11:18:17 jump-eu-001 sshd[20544]: Received disconnect from 101.50.60.253 port 55508:11: Bye Bye [preauth]") is None
    assert find_ip("Sep 24 11:18:17 jump-eu-001 sshd[20544]: Invalid user jackholdem from 101.50.60.100 port 55508") == "101.50.60.100"