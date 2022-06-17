#/bin/bash

# ask the team to run A or B? put in a variable $team
# get the lower version of $team
# get the filename starting with 'team_$team'
# if the extension is 'py' do 'python team_$team.py' to run the file
# if the extension is 'java' do 'java -c team_$team.java && java $team.out'

echo "Please enter your team name"
read -r team
#echo "Please enter your file extension(py / java)"
#read -r extension

filename=$(ls -1 | grep "team_$team")
extension=$(echo $filename | cut -d "." -f 2)

echo "[-] filename:  $filename"
echo "[-] extexion :  $extension"

run_python(){
    python $1
}

run_java(){
    java $1 && java $team.out
}

run_c(){
    gcc $1 && ./a.out
}

run_node(){
    node $1
}

run_ruby(){
    ruby $1
}

run_golang(){
    go run $1
}

run_cpp(){
    g++ $1 && ./a.out
}

if [[ "$filename" == *".py" ]]; then
    run_python $filename
elif [[ "$filename" == *".java" ]]; then
    run_java $filename
elif [[ "$filename" == *".cpp" ]]; then
    run_cpp $filename
elif [[ "$filename" == *".c" ]]; then
    run_c $filename
elif [[ "$filename" == *".js" ]]; then
    run_node $filename
elif [[ "$filename" == *".rb" ]]; then
    run_ruby $filename
elif [[ "$filename" == *".go" ]]; then
    run_golang $filename
fi
