#!/bin/bash

E_NOARGS=65

if [ -z "$1" ]; then
  echo "Usage: `basename $0` directory-to-copy to "
  exit $E_NOARGS
fi

ls . | xargs -i -t cp ./{} $1

exit 0
