#!/bin/bash

# Executa os testes com pytest e gera o relatório de cobertura em HTML
pytest --cov=filehandler --cov-report=html

# Diretório de relatórios de cobertura
COVERAGE_DIR=.

# Envia os relatórios de cobertura para o Codecov
curl -s https://codecov.io/bash | bash -s -- -t c74d0652-575f-49a4-b77e-7857f25d42e8 -f coverage.xml

# Abre a página index.html no navegador padrão
if which xdg-open > /dev/null; then
    xdg-open coverage_html_report/index.html
else
    echo "Não foi possível abrir a página. Verifique se um navegador está instalado e configurado corretamente."
    exit 1
fi
