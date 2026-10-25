# HiveBox

An end-to-end platform project built following the [Dynamic DevOps Roadmap](https://devopsroadmap.io/projects/hivebox/).
HiveBox tracks environment sensor data from [openSenseMap](https://opensensemap.org/).

The focus is the platform: containers, CI/CD, Kubernetes, Terraform, and observability.
The app code stays small on purpose.

<p align="center">
  <img src="https://devopsroadmap.io/img/hivebox-architecture.gif" width="60%" />
</p>

## Status

| Phase | Topic | Status |
|---|---|---|
| 1–2 | Kickoff, basics | done |
| 3 | Start: app, Docker, CI | planned |
| 4 | Kubernetes, CD | planned |
| 5 | Terraform, Helm, cache, E2E | planned |
| 6 | GitOps | planned |

## Run locally

Requires Docker. The version lives in `version.txt` ([Semantic Versioning](https://semver.org/)).

Build the image, tagged with the current version:

```bash
docker build -t hivebox:$(cat version.txt) .
```

Run it:

```bash
docker run --rm hivebox:$(cat version.txt)
```

Expected output (the app prints its version and exits with code 0):

```
v0.0.1
```

## Layout

```
app/     Python app and tests
k8s/     Kubernetes manifests
infra/   Terraform
docs/    Architecture notes and diagrams
```

## License

MIT
