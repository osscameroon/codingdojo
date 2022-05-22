# ask the team to run A or B? put in a variable $team
# get the lower version of $team
# get the filename starting with 'team_$team'
# if the extension is 'py' do 'python team_$team.py' to run the file
# if the extension is 'java' do 'java -c team_$team.java && java $team.out'

echo "Please enter your team name"
read -r team
#echo "Please enter your file extension(py / java)" 
#read -r extension

extension="py"
filename="team_$team.$extension"


# Qu'est-ce qu'on tente de tester ici ?
echo "Filename: $filename"
if [[ "$filename" == *".py" ]]; then
#  echo "I am py"
  python $filename;
elif [[ "$filename" == *".java" ]]; then
#  echo "I am java"
  java $filename && java $team.out;
fi