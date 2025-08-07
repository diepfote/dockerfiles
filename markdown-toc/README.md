# How to use


```
# docker run -w /data -v ~/Repos/diepfote.github.io/:/data -it localhost/markdown-toc bash
# TOP=1; for file in */*.md; do echo ---; echo "$file"; mdtoc.rb "$file" "$TOP"; done
```

e.g.

```
root@b4f7e634073a:/data# TOP=1; for file in */*.md; do echo ---; echo "$file"; mdtoc.rb "$file" "$TOP"; done
---
package-manager-helpers/index.md
#### Table of contents

1. [Darwin / Mac OS - brew](#darwin--mac-os---brew)
    - [brew formulae-require](#brew-formulae-require)
    - [brew required-by](#brew-required-by)
    - [brew leaves-require](#brew-leaves-require)
2. [Arch Linux - yay | pacman](#arch-linux---yay--pacman)
    - [yay-all](#yay-all)
    - [yay-generate-PKGBUILD-checksum](#yay-generate-pkgbuild-checksum)
        * [Why?  ](#why--)
---
projects/archlinux-container-like-full-arch.md
#### Table of contents

---
...
...
...
```
