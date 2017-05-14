#!/usr/bin/env bash

if hash python 2>/dev/null ; then
  if hash pip  2>/dev/null ; then

    v=$(python --version 2>&1 |awk '{print$2}')
    a=( ${v//./ } )   ## replace points, split into array
    ((a[2]++))        ## increment revision (or other part)

    ## composed as new version chain
    if [ '2.7' =  "${a[0]}.${a[1]}" ] ; then
      echo -e '[info] Python installed and correct!'
      exit
    fi
  fi
fi

echo -e 'Starting setup..'
if ! hash brew ; then
  echo -e '[info] Installing Homebrew'
  ruby -e "$(curl -fsSL https://goo.gl/uP5ePv)"
fi

echo -e '[info] Updating Homebrew'
brew update

echo -e '[info] Installing Python'
brew reinstall python

echo -e '[info] Installing PIP'
eval $(which easy_install |head -1 |awk '{print$3}') -U pip

echo -e '[info] Update successful'
exit
