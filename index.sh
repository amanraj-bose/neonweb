#!/bin/bash
clear
read -p "Enter The Name : " -s name
if ["$name" = ""];
then
     echo "Thanks for cloning and see my WEB"
     else
       echo "Access Denied :" 
fi

git clone -b main https://github.com/amanraj-bose/neonweb.git
