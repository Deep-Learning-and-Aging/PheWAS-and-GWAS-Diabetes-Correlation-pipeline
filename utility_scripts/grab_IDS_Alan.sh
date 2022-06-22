#!/bin/bash

ls /n/groups/patel/Alan/Aging/Medical_Images/images/Abdomen/Liver/Raw/ | cut -d'_' -f1 | sort -un > ../temp.txt

awk -F'\t' '{print $0" "$0}' ../temp.txt > ../Liver_in_sample_pop_IDs.txt

ls /n/groups/patel/Alan/Aging/Medical_Images/images/Abdomen/Pancreas/Raw/ | cut -d'_' -f1 | sort -un > ../temp.txt

awk -F'\t' '{print $0" "$0}' ../temp.txt > ../Pancreas_in_sample_pop_IDs.txt

rm ../temp.txt

# sed removes weird <<<<<<< line from file that is added, not sure why its added
cat ../Pancreas_in_sample_pop_IDs.txt ../Liver_in_sample_pop_IDs.txt | sort -un | sed '1d' > ../Abdomen_in_sample_pop_IDs.txt