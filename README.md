# Search

This model uses the twitter tweets dataset available from archiveteam twitter stream.  It's too big to commit, so to get the dataset and unzip it, run the folliwing commands:


```bash
wget https://archive.org/download/archiveteam-twitter-stream-2018-10/twitter-2018-10-01.tar
tar -xvf twitter-2018-10-01.tar
mv 2018/ dataset/
```

Once the test data is installed, you'll want to unzip the files, this can be done using the command:

```bash

```

We'll also be creating the app in a new docker container each time that we launch it.  To do this we'll need docker to be installed.  This can be achieved using the following commands:

Clean up:
```bash
sudo apt-get remove -y docker docker-ce docker-engine docker.io docker-compose golang-docker-credential-helpers
sudo apt autoremove -y
sudo rm -rf ~/.docker
```

Dependencies:
```bash
sudo rm -rf ~/.docker
tsudo apt-get install -ey apt-transport-https ca-certificates curl software-properties-common
```

Docker compose install:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
```


```bash
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/1.22.0/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
sudo usermod -a -G docker $USER
```
