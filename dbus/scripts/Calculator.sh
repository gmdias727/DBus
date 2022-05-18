#!/bin/bash

dbus-send --print-reply=literal --dest=org.example.Calculator /org/example/Calculator org.example.Calculator.Addition int32:2022 int32:1945

dbus-send --print-reply=literal -dest=org.example.Calculator /org/example/Calculator org.example.Calculator.Dolar