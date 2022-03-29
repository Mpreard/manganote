# MangaNote

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/Mpreard/manganote.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/Mpreard/manganote/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)
***

## Name
MangaNote

## Description
MangaNote is a tool to discover new manga and anime. It also allows you to mark the location (chapter or episode) of your readings / viewings.  

You can find this project in `www.manganote.nokram.store`

## Installation
### <u>Docker</u> 
`https://hub.docker.com/editions/community/docker-ce-desktop-windows/`

### <u>PostgreSql</u>
```
$ docker run --name manganote-pg -e POSTGRES_PASSWORD=pg -e POSTGRES_USER=pg -e POSTGRES-DB=manganote -p 5432:5432 -d postgres

$ docker exec -it manganote-pg bash

$ psql -U pg

$ CREATE DATABASE manganote;
```

### <u>Django</u>
```
$ python3.6 get-pip.py

$ pip install django

$ pip install psycopg2

$ pip install requests
```

### <u>Migrations</u>
```
$ python manage.py migrate
```

## Lancement
```
$ python manage.py runserver
```

## API
Kistu api est une api fournissant un catalogue de mangas / animés très complet. En plus de fournir ce catalogue, un ensemble de détails pour chaque manga / animé est proposé.  

Documentation : `https://kitsu.docs.apiary.io/`  

## Roadmap
- Add `My List` function
- Add `Notifications` function
- Add `Favorites` function
- /!\ Potential : Can see friend's reads/views

## Authors and acknowledgment
Simon GALOYAN   
Florian AUBIN  
Maël FOURNIER   
Maxime PREARD  

## License
No license

## Project status
This project is a student project in building phase.
