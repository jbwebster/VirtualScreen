
cd groups
rm list.txt
ls *.pdbqt > list.txt
cd ..
python moveIntoGroups.py groups/list.txt $1
cd groups
rm list.txt
for group in *
do
	rm $group/list.txt
	ls $group > $group/list.txt
done
rm ../grouplist.txt
ls > ../grouplist.txt
cd ..
rm setLists/*
python generateSets.py grouplist.txt

