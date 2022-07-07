#!/bin/bash

ls /n/groups/patel/Alan/Aging/Medical_Images/images/Abdomen/Liver/Raw/ | cut -d'_' -f1 | sort -un > ../in_pop_IDs/temp.txt

awk -F' ' '{print $0" "$0}' ../in_pop_IDs/temp.txt > ../in_pop_IDs/Liver_in_sample_pop_IDs.txt

ls /n/groups/patel/Alan/Aging/Medical_Images/images/Abdomen/Pancreas/Raw/ | cut -d'_' -f1 | sort -un > ../in_pop_IDs/temp.txt

awk -F' ' '{print $0" "$0}' ../in_pop_IDs/temp.txt > ../in_pop_IDs/Pancreas_in_sample_pop_IDs.txt

rm ../in_pop_IDs/temp.txt

# sed removes weird <<<<<<< line from file that is added, not sure why its added
cat ../in_pop_IDs/Pancreas_in_sample_pop_IDs.txt ../in_pop_IDs/Liver_in_sample_pop_IDs.txt | sort -un | sed '1d' > ../in_pop_IDs/Abdomen_in_sample_pop_IDs.txt

sed -e 's/ /\t/g' ../in_pop_IDs/Liver_in_sample_pop_IDs.txt > temp1.txt
sed -e 's/ /\t/g' ../in_pop_IDs/Pancreas_in_sample_pop_IDs.txt > temp2.txt
sed -e 's/ /\t/g' ../in_pop_IDs/Abdomen_in_sample_pop_IDs.txt > temp3.txt

mv temp1.txt ../in_pop_IDs/Liver_in_sample_pop_IDs.txt
mv temp2.txt ../in_pop_IDs/Pancreas_in_sample_pop_IDs.txt
mv temp3.txt ../in_pop_IDs/Abdomen_in_sample_pop_IDs.txt