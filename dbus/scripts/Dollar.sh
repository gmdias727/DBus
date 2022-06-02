#!/bin/bash

while true;
do
    dollarValue=$(dbus-send --print-reply=literal --dest=dollar.quote.DollarToday /dollar/quote/DollarToday dollar.quote.DollarToday.TodaysDollarToBRL)
    filePath='/home/finalproject/Desktop/DBus/dbus/data/TodaysDollarValueToBRL.txt'
    output="Dollar current quote is: R\$${dollarValue//[[:blank:]]/}."
    echo -e "$output" > "$filePath"
    cat "$filePath" 
    sleep 5;
done
