rm -r fragments
mkdir fragments
#workFile='pg/author1/work.txt'
workFile="$1"
authorId="$2"
workId="$3"
split  --additional-suffix=".frg" -a 5 -d -l 10 "$workFile" fragments/fragment-"$authorId"-"$workId"- 
#fragmnets
