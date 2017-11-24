#!/bin/bash

set -ue

if [ ! -e samples ]; then
  mkdir -p samples
fi

git clone https://github.com/takahasi/ImageDataCollector.git samples/ImageDataCollector
git clone https://github.com/tonboAkinori/NameToVelocity.git samples/NameToVelocity

exit 0
