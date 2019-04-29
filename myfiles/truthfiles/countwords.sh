#!/bin/bash

file='trinitate151-195.txt'

word='Πέτρον'
word='Πέτρος'
word='αὐτὸν'
word='ἀφέωνταί'
word='θεοῦ'
word='Ἰησοῦ'
word='εὐαγγέλιον'
word='καὶ'

word='Χριστοῦ'

#word='πνεῦμα'

word="$1"

#cat "$file"|tr " " "\n"|sort|uniq -c|sort
#cat "$file"|tr " " "\n"|sort|uniq -c|sort>test.txt

 
cat "$file"|tr " " "\n"|sort|uniq -c|\
sed -rn 's@'$word'@'$word'@gp'

