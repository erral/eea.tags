#!/bin/sh
PRODUCTNAME='eea.tags'
I18NDOMAIN=$PRODUCTNAME

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/${PRODUCTNAME}-manual.pot locales/*/LC_MESSAGES/${PRODUCTNAME}.po



