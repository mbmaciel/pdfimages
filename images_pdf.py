#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# >>> gera_pdf.py  - 04/09/2012
# Por Mauricio Maciel <mbmaciel@linuxdepot.com.br>
# Gerador de pdf das imagens no diretorio. Utiliza o report lab.
# Reportlab - http://www.reportlab.com/software/opensource/
# Instalação - sudo easy_install reportlab
 
import os
import random
import string
from reportlab.pdfgen import canvas
 
 
#variaveis
dir = os.getcwd()
 
def file_generator(size=6, chars=string.ascii_lowercase + string.digits):
    '''
    Função gera o nome aleatorio
    '''
    word = ''.join(random.choice(chars) for x in range(size))
    return 'file'+word+'.pdf'
 
def pdfDirectory(imageDirectory, outputPDFName=file_generator()):
    '''
    Função gera o PDF
    '''
    dirim = str(imageDirectory)
    output = str(outputPDFName)
 
    c = canvas.Canvas(output, pagesize=(425,283))
    try:
        for root, dirs, files in os.walk(dirim):
            for name in files:
                lname = name.lower()
                if lname.endswith(".jpg") or lname.endswith(".gif") or lname.endswith(".png"):
                    filepath = os.path.join(root, name)
                    c.drawImage(filepath, 0, 1, width=425, height=283)
                    c.showPage()
                    c.save()
 
        print "PDF das imagens criado!"
    except:
        print "Falha ao gerar PDF"
 
 
# modo de usar
pdfDirectory(dir)

