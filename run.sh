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

declare -A extToCommand=( \
    [py]="python $filename" \
    [java]="java $filename && java $team.out" \
    [c]="gcc $filename && ./a.out"\
)

echo $(${extToCommand[$extension]})
