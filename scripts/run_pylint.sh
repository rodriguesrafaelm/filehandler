#!/bin/sh

if [ ! -d "logs" ]; then
    # Se a pasta não existir, cria a pasta "logs"
    mkdir logs
    echo "Pasta 'logs' criada."
else
    echo "A pasta 'logs' já existe."
fi

pylint ../filehandler > ./logs/pylint.log 2>&1
