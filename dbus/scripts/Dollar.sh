#!/bin/bash
while true;

do
    dollarValue=$(dbus-send --print-reply=literal --dest=dollar.quote.DollarToday /dollar/quote/DollarToday dollar.quote.DollarToday.TodaysDollarToBRL)
    output="Dollar current quote is: $dollarValue BRL."
    echo -e "$output" > TodaysDollarValueToBRL.txt
    sleep 15;
    echo -e "$output"
done
