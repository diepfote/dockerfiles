# How to use

Lint a directory

```
$ docker run -v "$PWD":/data -w /data --rm -it markdown-lint  bash
root@55ce1d18ba8a:/data# find -name '*.md' -exec sh -c 'mdl "$0"' {} \;

# or
$ docker run -v "$PWD":/data -w /data --rm -it markdown-lint  mdl . 
...
./gif.md:12: MD009 Trailing spaces
./gif.md:16: MD012 Multiple consecutive blank lines
./gif.md:17: MD012 Multiple consecutive blank lines
./gif.md:5: MD036 Emphasis used instead of a header
./fzf.md:10: MD012 Multiple consecutive blank lines
./fzf.md:7: MD013 Line length
./fzf.md:1: MD022 Headers should be surrounded by blank lines
./fzf.md:3: MD022 Headers should be surrounded by blank lines
./fzf.md:4: MD031 Fenced code blocks should be surrounded by blank lines
```
