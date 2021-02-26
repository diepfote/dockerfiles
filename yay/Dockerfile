FROM archlinux/base

# FYI: ldns includes drill
RUN pacman --noconfirm -Syyu --needed git vi neovim man man-pages sudo \
    base-devel pkgfile ldns

# build man database
RUN mandb

# initialize pkgfile database
RUN pkgfile -u

# ----------
# yay cannot be run as root!
#
# taken from: https://github.com/justin8/docker-makepkg/blob/master/Dockerfile
#
ADD sudoers /etc/sudoers
RUN useradd -m -d /build build-user
WORKDIR /build
RUN sudo -u build-user git clone https://aur.archlinux.org/yay.git; cd yay; sudo -u build-user makepkg -sri --noconfirm
# ----------
#
