# ManganatoFlix

This is a minimalistic line bash script that allows you to download and open a downloaded version of the manga of your choice. 

It uses zathura but that can be easily changed. 

It downloads it in `$HOME/Documents/torrent/manga` (yes I know it is not torrenting but still) but that directory can be changed by changing varible `DOWNLOAD_DIR`.

Overall it is very customizable.

*It is made to be used on linux.

## Dependencies

- zathura 
- zathura-pdf-poppler or zathura-pdf-mupdf
- pup 

## Usage

`mangaflix _name_of_manga_ _chapter_number_`

for example

`mangaflix boruto 67`

## Download 

### Git (Reccomended as you can update easily)

```sh
git clone https://github.com/ThamognyaKodi/FlixTools.git

cd FlixTools/ManganatoFlix

sudo make install
```

#### To update

```sh
cd _directory_to_FlixTools_/FlixTools

git pull

cd ManganatoFlix 

sudo make install
```

### Curl

```sh
curl -Lo mangaflix https://raw.githubusercontent.com/ThamognyaKodi/FlixTools/master/ManganatoFlix/mangaflix

mv mangaflix /usr/local/bin/mangaflix
```

#### To Update

```sh
cd /usr/local/bin

sudo rm mangaflix 

sudo curl -Lo mangaflix https://raw.githubusercontent.com/ThamognyaKodi/FlixTools/master/ManganatoFlix/mangaflix
```

### AUR

comming soon

### Gentoo Ebuild

comming soon

## Code

You may be wondering why I have grouped all of those lines together. Firstly to make it 5 lines and secondly since each line has a unique purpose

## issues and PRs

Make an issue and PR if there is something wrong or you want to change something, and I will take a look at it.

##### Documentation under work
