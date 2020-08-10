<div align="center">
   <img width="250" src="https://i.imgur.com/3yzjjhx.png" alt="logo"></br><h2>Mashupy</h2>

[![](https://img.shields.io/cpan/v/HTTP-Message)](https://metacpan.org/pod/Term::ANSIColor) [![CodeFactor](https://www.codefactor.io/repository/github/sinkaroid/Mashupy/badge)](https://www.codefactor.io/repository/github/sinkaroid/Mashupy) [![Build Status](https://travis-ci.com/sinkaroid/Mashupy.svg?branch=master)](https://travis-ci.com/sinkaroid/Mashupy) [![Python 3](https://pyup.io/repos/github/sinkaroid/Mashupy/python-3-shield.svg)](https://pyup.io/repos/github/sinkaroid/Mashupy/)  

----
</div>

## Mashupy
  
Bulk request according wordlist any [shells/params/files/port]  
in this case i using for scan any shells and parameter.  
adjust all ya needs yourself.  


## Smol and Lightweight.
no need many modules to init from any VPs/shell or any environment.  
with some different implementation.  
just make issues or Pr if u had a trouble according OS

## defines

| Key                 | Description                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
|`mashu pl           `| single request (perl)                                                                            |
|`mashu py           `| single request (python)                                                                          |
|`mass               `| bulk request (python 3)                                                                          |
|`massq              `| bulk request (python 2)                                                                          |
|`list               `| selftarget (separated with break lines)                                                          |
|`word               `| selfwordlist (separated with break lines)                                                        |
|`res                `| logs and output                                                                                  |
|`lacur.log          `| readbale logs                                                                                    |
  

## tested on
[![Linux Ubuntu](https://img.shields.io/badge/Linux-Ubuntu-orange.svg)](/Screenshot/Screenshot_2020-08-06_08-09-28.png)
[![Linux Debian](https://img.shields.io/badge/Linux-Debian-blue.svg)](/Screenshot/Screenshot_2020-08-05_23-20-41.png)
[![Linux backbox](https://img.shields.io/badge/Linux-Backbox-darkblue.svg)](/Screenshot/Screenshot_2020-08-06_08-09-28.png)
[![Windows](https://img.shields.io/badge/Win10_64-Canary-lightblue.svg)](/Screenshot/Screenshot_606.png)  
## Run
make sure init yer any wordlist and target in [/init](/init/)  
root is optional,

clone this repo or with pip (if possible)

----

     $ pip install -r requirements.txt  
     $ ./mashu

## hook
send any logs
```sh
hook='discordhooks url'
isi='all ya need here'

url=${hook}
curl -H "Content-Type: application/json" \
-X POST \
-d '{"username": "Mashu", "content": "'${isi}'"}' $url
```

### Further:

- [docs.python.org/3/library/http.client.html](https://docs.python.org/3/library/http.client.html) HTTP protocol client
- [metacpan.org/pod/HTTP::Request](https://metacpan.org/pod/HTTP::Request) Perl HTTP::Request
- Artwork [先輩と南国デート](https://www.pixiv.net/en/artworks/79277843) by [@Ayul@お仕事募集中](https://www.pixiv.net/en/artworks/79277843)
- avoid bad request or anything else,recommend to run dis tools with `root` access [optional]
- `colorama` disable or remove dat if there's nothing root/privilege to install module

### Tester/Contributor
| [<img src="https://avatars1.githubusercontent.com/u/12372481?s=460&u=4b4ff2fadbdb04dd9534286e8cfe3a34a8586fe1&v=4" width="40px;"/><br /><sub><b>Sinkaroid</b></sub>](https://github.com/sinkaroid)<br />💻🐛|[<img src="https://avatars1.githubusercontent.com/u/19934508?s=460&v=4" width="40px;"/><br /><sub><b>Seringh</b></sub>](https://github.com/p3arce)<br /> 🐛|[<img src="https://avatars1.githubusercontent.com/u/65139960?s=200&v=4" width="40px;"/><br /><sub><b>Redsplit</b></sub>](https://github.com/Redsplit)<br /> 🔧
| :---: | :---: | :---: |
### eof

- feel free to make PR, maybe this tools just using `sucks` pattern and `weird` implementation, if u have more good ideas than this one, just PR.
- I am not responsible whether this is used for illegality or any cases that shells were stabbed from user to another user.

