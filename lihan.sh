read -p "Nama file>> " file
echo
echo
read -p "url web>> " host
echo
python2 nf.py $host $file
