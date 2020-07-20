FROM archlinux/base

RUN pacman --noconfirm -Syyu
RUN pacman --noconfirm -S --needed git vim man man-pages sudo base-devel pkgfile
RUN mandb
#RUN pacman --noconfirm -S --needed xfce4

# taken from: https://github.com/justin8/docker-makepkg/blob/master/Dockerfile
ADD sudoers /etc/sudoers
RUN useradd -m -d /build build-user
WORKDIR /build

RUN sudo -u build-user git clone https://aur.archlinux.org/yay.git; cd yay; sudo -u build-user makepkg -sri --noconfirm

