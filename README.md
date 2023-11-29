## Python Flask app
- Simple Python Flask app that uses a database via docker
- Uses two public APIs
    - One that provides dog facts and the other provides cat facts
    - When facts are provided, the last 3 persist via the database

### Setup
- Copy `sample.envrc` to `.envrc`
```
cp sample.envrc .envrc
```
- Setup postgres via docker compose:
```
docker compose up -d
```
- Build image via `Dockerfile`
```
docker build -t poetryanimaldb:1.0 .
```
- Run a new container with built image
    - This uses the network that was built via `docker compose` and exposes the port `5000`
```
docker run --network poetryanimalfactsdb_python -p 5000:5000 poetryanimaldb:1.0
```
