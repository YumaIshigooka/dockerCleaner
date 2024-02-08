# dockerCleaner
Clean all `<none>` images, and their respective stopped container that was running it, not allowing to delete the images.

## Run Locally

Clone the project

```bash
  git clone https://github.com/YumaIshigooka/dockerCleaner.git
```

Go to the project directory

```bash
  cd dockerCleaner
```

Run the script

```bash
  python3 cleanDocker.py
```
or 
```bash
  sudo python3 cleanDocker.py
```
if superuser access is needed to run docker.

