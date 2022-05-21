#!/bin/bash

    echo """
    What operation do you want?
    
    Option 1: Addition
    Option 2: Subtraction
    Option 3: Multiplication
    Option 4: Division
    """
    sleep 1;

    read -r -p "Choose your operation: " operator
    if [[ "$operator" -eq 1 ]]
        then
            echo "You selected addition operator $operator"
            operation="Addition"
            
    fi
    if [[ "$operator" -eq 2 ]]
        then 
            echo "You selected subtraction."
            operation="Subtraction"
    fi
    if [[ "$operator" -eq 3 ]]
        then 
            echo "You selected multiplication."
            operation="Multiplication"
    fi
    if [[ "$operator" -eq 4 ]]
        then 
            echo "You selected division."
            operation="Division"
    fi
    sleep 1;

    read -r -p "Input a integer number: " num1

    while [[ $num1 == ^[0-9]+$ ]]
        do
            echo "Invalid number"
            read -r -p "Try again, input a integer number: " num1
    done

    read -r -p "Input another integer number: " num2
    
    while [[ $num2 == ^[0-9]+$ ]]
        do 
            echo "Invalid number"
            read -r -p "Try again, input a integer number: " num2
    done

dbus-send --print-reply=literal --dest=org.example.Calculator /org/example/Calculator org.example.Calculator."$operation" int32:"$num1" int32:"$num2"