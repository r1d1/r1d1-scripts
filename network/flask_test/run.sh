#!/bin/bash

export FLASK_APP=minimal
export FLASK_ENV=development

flask run $1

echo "Server ended"
