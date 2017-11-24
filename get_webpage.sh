#!/bin/bash

set -ue

sudo apt-get install wkhtmltopdf

function get()
{
  wkhtmltopdf $1 $2
  return
}

if [ ! -e web ]; then
  mkdir -p web
fi

get http://openrtm.org/openrtm/ja/node/6386 web/tutorial-2-win.pdf
get http://openrtm.org/openrtm/ja/node/6387 web/tutorial-2-linux.pdf
get http://openrtm.org/openrtm/ja/node/6388 web/tutorial-3a.pdf
get http://openrtm.org/openrtm/ja/node/6389 web/tutorial-3b.pdf

exit 0
