#!/bin/bash

while true;
do
    dollarValue=$(dbus-send --print-reply=literal --dest=dollar.quote.DollarToday /dollar/quote/DollarToday dollar.quote.DollarToday.TodaysDollarToBRL)
    filePath='/home/grandehe4rt/dev/faculdade/DBus/dbus/data/TodaysDollarValueToBRL.txt'
    output="Dollar current quote is: R\$${dollarValue//[[:blank:]]/}."
    echo -e "$output" > "$filePath"
    echo -e "$output"

    echo 
    sleep 10;
done



