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

# Abre a página index.html no navegador padrão
if which xdg-open > /dev/null; then
    xdg-open ./logs/coverage_html_report/index.html
else
    echo "Não foi possível abrir a página. Verifique se um navegador está instalado e configurado corretamente."
    exit 1
fi
