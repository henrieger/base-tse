#!/bin/bash

for state in "AC" "AL" "AP" "AM" "BA" "CE" "DF" "ES" "GO" "MA" "MT" "MS" "MG" "PA" "PB" "PR" "PE" "PI" "RJ" "RN" "RS" "RO" "RR" "SC" "SP" "SE" "TO" "Exterior"
do
    for year in 2018 2021
    do
        echo "Transferindo arquivo "$state"_"$year".csv"

        # script python webscrapper
        python3 scrapper.py $state $year

        # move o arquivo para pasta local
        mv ~/Downloads/eleitores_filiados.csv estados/

        # substitui a codificação do arquivo para UTF-8 e altera seu nome
        ENCODING=$(file -i estados/eleitores_filiados.csv | cut -d';' -f2 | cut -d= -f2)
        iconv -f ${ENCODING^^} -t UTF-8 estados/eleitores_filiados.csv -o estados/$state\_$year.csv
        rm estados/eleitores_filiados.csv

        # retira ';' desnecessário do final do cabeçalho
        FIRST_LINE=$(head -n 1 estados/$state\_$year.csv)
        if [[ ${FIRST_LINE: -1} == ';' ]]; then
            sed -i "1s/.*/${FIRST_LINE::-1}/" estados/$state\_$year.csv
        fi

        # Retira '.' dos números na casa dos milhares
        CONT_ARQ=$(cat estados/$state\_$year.csv)
        echo "${CONT_ARQ//'.'/''}" > estados/$state\_$year.csv
    done
done

echo ""

# script python final
python3 extrai_dados.py