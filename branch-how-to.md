# What is branches on Git?

Branches in git allows you to work on different versions of program, not breaking main branch (usually 'main' or 'master'). For example you can have branches main - for release and develop - for some features, which have not been tested

# How to make branch?

For new brench in your repo you should write in terminal

```sh
git branch <name>
```

Or you can make new branch and connect to it instantly using:

```sh
git checkout -b <name>
```

# How to connect to the branch?

For connecting to the branch you can use next command:

```sh
git checkout <name>
```

# How to send branch on server?

For pushing you branch on server you should use next command:

```sh
git push -u origin <name>
