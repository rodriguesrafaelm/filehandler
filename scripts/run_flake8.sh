#!/bin/sh

if [ ! -d "logs" ]; then
    # Se a pasta não existir, cria a pasta "logs"
    mkdir logs
    echo "Pasta 'logs' criada."
else
    echo "A pasta 'logs' já existe."
fi
mkdir -p logs/flake8_report
echo "Pasta 'logs/flake8_report' criada."
flake8 --config=.flake8 --format=html --htmldir=logs/flake8_report