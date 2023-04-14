#!/bin/bash

echo "Criando diretórios..."

mkdir /publico
mkdir /adm
mkdir /sec
mkdir /ven

echo "Diretórios criados com sucesso!"

echo "Criando grupos de usuários..."

groupadd GRP_ADM
groupadd GRP_SEC
groupadd GRP_VEN

echo "Grupos de usuários criados com sucesso!"

echo "Criando usuários..."

useradd carlos -c "Carlos" -m -s /bin/bash -p Senha369 -G GRP_ADM
useradd joao -c "João" -m -s /bin/bash -p Senha369 -G GRP_ADM
useradd maria -c "Maria" -m -s /bin/bash -p Senha369 -G GRP_ADM

useradd amanda -c "Amanda" -m -s /bin/bash -p Senha369 -G GRP_SEC
useradd josefina -c "Josefina" -m -s /bin/bash -p Senha369 -G GRP_SEC
useradd rogerio -c "Rogerio" -m -s /bin/bash -p Senha369 -G GRP_SEC

useradd debora -c "Debora" -m -s /bin/bash -p Senha369 -G GRP_VEN
useradd roberto -c "Roberto" -m -s /bin/bash -p Senha369 -G GRP_VEN
useradd sebastiana -c "Sebastiana" -m -s /bin/bash -p Senha369 -G GRP_VEN

echo "Usuários criados com sucesso!"

echo "Especificando permissões dos diretórios..."

chown root:GRP_ADM /adm
chown root:GRP_SEC /sec
chown root:GRP_VEN /ven

chmod 770 /adm
chmod 770 /sec
chmod 770 /ven
chmod 777 /publico

echo "Permissões configuradas com sucesso!"

echo "Fim!"
