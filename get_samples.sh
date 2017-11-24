#!/bin/bash

set -ue

if [ ! -e sample ]; then
  mkdir -p sample
fi

function get()
{
  git clone --depth 1 $1 sample/`basename $1`
  rm -rf sample/`basename $1`/.git
  return
}

get https://github.com/takahasi/ImageToObjectPrediction
get https://github.com/takahasi/ImageDataCollector
get https://github.com/tonboAkinori/NameToVelocity

exit 0
