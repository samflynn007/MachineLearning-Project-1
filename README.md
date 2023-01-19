# MachineLearning-Project-1
This  is first machine learning project

1. [Github Account](https://github.com)
2. [Render Account](https://dashboard.render.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git cli](https://git-scm.com/downloads)


Creating Conda Environment 
```
conda create -p venv python==3.7 -y
 ```

```
conda activate venv/
```
pip install -r requirements.txt
```
git status 
```
To check the git status
```
git log
```
To check all version maintained by git

To Add file to git

```
git add .
```
or

```
git add <file_name>
```
To create version/ commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```
To setup CI/CD pipeline in render we need 3 information
1. RENDER_EMAIL = sww@gmail.com
2. RENDER API_KEY = <>
3. RENDER_APP_NAME = <>

BUILD DOCKER IMAGE

```
docker build -t <image_name>:<tagname> .
```
> Note : Image name for docker must be lowercase
To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker

```
docker ps
```
Tos stop docker conatiner
```
docker stop <container_id>
```
```
python setup.py install
```

Install ipykernel
```
pip install ipykernel
```