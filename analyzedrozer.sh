#!/bin/bash

if [ $1 == 'list' ]; then
	drozer console connect -c "run app.package.list -f $2"
	exit 0
fi

echo "==============================="
echo "======= APP INFORMATION ======="
echo "==============================="

drozer console connect -c "run app.package.info -a $1"

echo "==============================="
echo "======= ATTACK SURFACES ======="
echo "==============================="

drozer console connect -c "run app.package.attacksurface $1"

echo "==============================="
echo "======= ACTIVITIES INFO ======="
echo "==============================="

drozer console connect -c "run app.activity.info -a $1"

echo "==============================="
echo "======= PROVIDERS INFO ========"
echo "==============================="

drozer console connect -c "run app.provider.info -a $1"

echo "==============================="
echo "======== PROVIDER SCAN ========"
echo "==============================="

drozer console connect -c "run scanner.provider.finduris -a $1"

echo "==============================="
echo "======== SERVICES INFO ========"
echo "==============================="

drozer console connect -c "run app.service.info -a $1"

echo "==============================="
echo "== BROADCAST RECEIVERS INFO ==="
echo "==============================="

drozer console connect -c "run app.broadcast.info -a $1"


