#!/bin/bash

# 1.-Descarga
echo -e "\nDescargando repositorio..."
sudo git clone https://github.com/OCA/l10n-spain.git -b 10.0 /opt/odoo/l10n-spain

# 2.-Acceso directo
echo -e "\nCreando los acceso directo..."
sudo ln -s /opt/odoo/l10n-spain/l10n_es_toponyms /opt/odoo/custom/addons
