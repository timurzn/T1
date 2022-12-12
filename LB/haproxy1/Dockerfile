FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    keepalived \
    haproxy \
    && rm -rf /var/lib/apt/lists/*


ENTRYPOINT keepalived -f /etc/keepalived/keepalived.cfg && haproxy -f /usr/local/etc/haproxy/haproxy.cfg