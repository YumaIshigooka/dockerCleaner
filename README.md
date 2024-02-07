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

Run the script (will ask for permissions, check the source code to ensure the reason)

```bash
  python3 cleanDocker.py
```

If you know how to remove the need of admin privileges, let me know.

