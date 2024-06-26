#!/bin/bash

# Executa os testes com pytest e gera o relatório de cobertura em HTML
pytest --cov=filehandler --cov-report=html

# Diretório de relatórios de cobertura
COVERAGE_DIR=.

if [ ! -d "logs" ]; then
    # Se a pasta não existir, cria a pasta "logs"
    mkdir logs
    echo "Pasta 'logs' criada."
else
    echo "A pasta 'logs' já existe."
fi