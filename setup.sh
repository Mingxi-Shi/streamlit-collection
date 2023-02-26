mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"muenchshi@gmail.com\"\n\
" > ~/.streamlit/credentials.toml


echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\

[deprecation]\n\
showPyplotGlobalUse = false\n\
" > ~/.streamlit/config.toml

wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar xvzf ta-lib-0.4.0-src.tar.gz
cd ta-lib-0.4.0
./configure --prefix=/usr
make
sudo make install
cd ..