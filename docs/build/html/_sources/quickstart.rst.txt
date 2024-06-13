========================
Guia de Início Rápido
========================

Instalação
==========

Para instalar o FileHandler, você pode usar o pip:

.. code-block:: shell

   pip install filehandler

Primeiros Passos
================

Aqui está um exemplo simples de como usar o FileHandler para realizar operações básicas de leitura e escrita de arquivos de texto, CSV, JSON e XML.

Leitura e Escrita de Arquivos de Texto
--------------------------------------

.. code-block:: python

   from filehandler.file_operations import read_text_file, write_text_file

   # Escrevendo em um arquivo de texto
   write_text_file("example.txt", "Olá, Mundo!")

   # Lendo do arquivo de texto
   conteudo = read_text_file("example.txt")
   print(conteudo)  # Saída: Olá, Mundo!

Leitura e Escrita de Arquivos CSV
---------------------------------

.. code-block:: python

   from filehandler.file_operations import read_csv_file, write_csv_file

   # Dados para escrever no arquivo CSV
   rows = [
       ["Nome", "Idade", "Cidade"],
       ["Alice", "30", "Nova York"],
       ["Bob", "25", "Los Angeles"]
   ]

   # Escrevendo em um arquivo CSV
   write_csv_file("example.csv", rows)

   # Lendo do arquivo CSV
   conteudo_csv = read_csv_file("example.csv")
   for row in conteudo_csv:
       print(row)

Leitura e Escrita de Arquivos JSON
----------------------------------

.. code-block:: python

   from filehandler.file_operations import read_json_file, write_json_file

   # Dados para escrever no arquivo JSON
   data = {
       "nome": "Alice",
       "idade": 30,
       "cidade": "Nova York"
   }

   # Escrevendo em um arquivo JSON
   write_json_file("example.json", data)

   # Lendo do arquivo JSON
   conteudo_json = read_json_file("example.json")
   print(conteudo_json)

Leitura e Escrita de Arquivos XML
---------------------------------

.. code-block:: python

   import xml.etree.ElementTree as ET
   from filehandler.file_operations import read_xml_file, write_xml_file

   # Criando um elemento XML
   root = ET.Element("root")
   child = ET.SubElement(root, "child")
   child.text = "Este é um exemplo"

   # Escrevendo em um arquivo XML
   write_xml_file("example.xml", root)

   # Lendo do arquivo XML
   root_lido = read_xml_file("example.xml")
   print(ET.tostring(root_lido, encoding="unicode"))

Este guia de início rápido deve fornecer uma boa visão geral sobre como usar as funcionalidades básicas do FileHandler. Para informações mais detalhadas, consulte as seções específicas da documentação.
