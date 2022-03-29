echo " "
echo "updating sys first"
sleep 2
pkg -y update
check_Packages() {
for i in python3 php cowsay git figlet; do
	dpkg -s $i &> /dev/null
	if [[ $? -eq 0 ]]; then
		echo -e "\e[1;32m[\e[\e[1;92m+\e[1;33m]\e[1;92m${i}\e[0m is Installed"
	else
		echo -e "\e[1;34m[\e[1;31m-\e[1;34m]\e[1;31m${i}\e[0m is not Installed"

	fi

done
}
install_Packages() {
for i in python3 php cowsay git figlet; do
	dpkg -s $i &> /dev/null
	if [[ $? -eq 0 ]]; then
		echo ""
	else
		echo ""
		echo -e "\e[1;38m[\e[\e[1;35m!\e[1;38m]Installing ${i}………………\e[1;34m[\e[1;32mPlease wait!\e[1;34m]\e[0m"
		sleep 1s
		apt-get install ${i} -y &> /dev/null
                pip3 install lolcat -y &> /dev/null
		echo ""
		echo -e "\e[1;31m[\e[1;92m+\e[1;33m]\e[1;32m${i}\e[0m Installed Successfully"
	fi
done
}

clear
sleep 1
check_Packages
sleep 2
install_Packages
sleep 2
figlet -c "thankyou" | lolcat
echo "to run the main tool type"
echo "$python3 gen.py"
sleep 4
clear
