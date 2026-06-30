# clone the project
# git clone url
# how to check currently which branch you are in 
# git status (python_basics (main))
# how to create a new branch
# git checkout -b branch-name(ex:git_basics)
#  check at which you are in
# git status
# how to checkout from one branch to another branch
# git checkout branch_name


#                 from
# python_basics ----------> git_basics ---> git status
#       from
# main --------> git_steps


# how to add the files to github(remote which is in github.com)
# git add .
# how to commit the new files or changes any code in to github
# git commit -m "AB#123:git basics"
# how to push the code from your local system newely created branch to remote repository as a new branch
# git push origin branch_name (ex: git_basics)

# 3 team members
# main branch ------> complete branch --> payments code 
# dwarkesh ---> orders branch (no payments code)---> orderbranch --> still he is working 
# kartheya ---> payment branch --> pull request --> resolved pr comments --> merge main branch
# devlopers---> pushed the code ---> merged 

# every day your branch must be updated with main branch code
# git pull origin branch_name(ex : main)
# git stash 

# dwarkesh ---> orders(pulled code main branch)   ---> only one file --> there is a chance of conflits, both are changing on single function
# ---> 

# kartheya ---> payment orders --> only one file ---> merged --> main
# dwarkesh
# need to pull the latest code from main branch
# git stash ---> save orders code in memory
# git status --> empth there is no changed files
# git pull origin main
# dwarkesh has updated code because he pulled the code from main branch
# doesn't have order's code & that code is in stash list(memory)
# git stash apply stash@{0} / git stash apply (recent stash will apply here)

