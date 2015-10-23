#!/bin/bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
curl -o node-v4.2.1.pkg https://nodejs.org/dist/v4.2.1/node-v4.2.1.pkg
sudo installer -pkg node-v4.2.1.pkg -target /
npm install react-tools --save-dev
npm install react --save-dev
npm install gulp --save-dev
npm install react browserify reactify vinyl-source-stream --save-dev
npm install babel-core --save-dev
virtualenv venv
. venv/bin/activate
pip install flask
pip install pymongo
pip install wtforms
pip install flask-wtf