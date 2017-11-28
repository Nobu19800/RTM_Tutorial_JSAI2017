#!/bin/bash

set -ue

if [ ! -e packages ]; then
  mkdir -p packages
fi

function get_chainer()
{
  wget https://github.com/chainer/chainer/archive/v$1.zip -O packages/chainer-v$1.zip
  return
}

function get_opencv()
{
  wget https://github.com/opencv/opencv/releases/download/$1/opencv-$1-vc14.exe -O packages/opencv-$1-vc14.exe
  return
}

function get_openrtm()
{
  wget http://openrtm.org/pub/Windows/OpenRTM-aist/1.1/OpenRTM-aist-$1.msi -O packages/OpenRTM-aist-$1.msi
  return
}

function get_python()
{
  wget https://www.python.org/ftp/python/`echo $1 | sed "s/\.amd64//"`/python-$1.msi -O packages/python-$1.msi
  return
}

function get_pyyaml()
{
  wget http://pyyaml.org/download/pyyaml/PyYAML-$1.exe -O packages/PyYAML-$1.exe
  return
}

function get_cmake()
{
  wget https://cmake.org/files/v3.5/cmake-$1.msi -O packages/cmake-$1.msi
  return
}

function get_doxygen()
{
  wget http://ftp.stack.nl/pub/users/dimitri/doxygen-$1-setup.exe -O packages/doxygen-$1-setup.exe
  return
}

get_chainer 3.0.0
get_chainer 2.1.0
get_opencv 3.3.1
get_opencv 2.4.13.3
get_openrtm 1.1.2-RELEASE_x86
get_openrtm 1.1.2-RELEASE_x86_64
get_python 2.7.10
get_python 2.7.10.amd64
get_pyyaml 3.11.wim32-py2.7
get_pyyaml 3.11.wim-amd64-py2.7
get_cmake 3.5.2-win32-x86
get_doxygen 1.8.11

exit 0
