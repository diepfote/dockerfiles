FROM lscr.io/linuxserver/calibre:7.26.0

# disable root
RUN sed -i 's|^root:.*:\/bin\/.*|root:x:0:0:root:/root:/usr/sbin/nologin|' /etc/passwd
RUN passwd -l root

USER 1000

ENTRYPOINT ["/usr/bin/ebook-convert"]


