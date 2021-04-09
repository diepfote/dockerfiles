FROM archlinux/base

# disable space check in pacman
RUN sed -i '/CheckSpace/d' /etc/pacman.conf

RUN pacman --noconfirm -Syyu
RUN pacman --noconfirm --needed -S zathura zathura-pdf-poppler diffpdf

