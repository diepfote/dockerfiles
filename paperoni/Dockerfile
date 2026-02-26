FROM ubuntu:20.04

# Avoid interactive tzdata etc.
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        libssl1.1 \
        libgcc-s1 \
        libc6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY paperoni_0.6.1_alpha1_x86_64.tar.gz /build/

# based on `PKGBUILD` in https://github.com/hipstermojo/paperoni/releases/tag/v0.6.1-alpha1
RUN sha256sum paperoni_0.6.1_alpha1_x86_64.tar.gz | awk '{ print $1 }' > calc_sha.txt
RUN test "$(head -n1 calc_sha.txt)" = 98cead719a41b34b4f4945d3778477b963fd345d014a3fb70a0a6209aca8c2f9
RUN tar xfz paperoni_0.6.1_alpha1_x86_64.tar.gz
RUN chmod +x paperoni
RUN mv paperoni /usr/local/bin/

RUN mkdir /data
RUN chown -R 1000:1000 /data
WORKDIR /data

ENTRYPOINT ["paperoni"]

