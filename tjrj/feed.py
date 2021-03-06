#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import datetime
import codecs

import jinja2

env = jinja2.Environment(loader=jinja2.PackageLoader('tjrj', 'templates'))

def gerar(processo):
    template = env.get_template("feed.xml")
    return template.render(processo=processo, agora=datetime.datetime.utcnow())

def salvar(processo, diretorio):
    xml = gerar(processo)

    arquivo = codecs.open(os.path.join(diretorio, processo.numero + ".xml"), "w", encoding="utf-8")
    arquivo.write(xml)
