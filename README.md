# HiveBox

An end-to-end platform project from the [Dynamic DevOps Roadmap](https://devopsroadmap.io/).
HiveBox tracks environment sensor data from [openSenseMap](https://opensensemap.org/).

The focus is the platform: containers, CI/CD, Kubernetes, Terraform, and observability.
The app code stays small on purpose.

## Status

| Phase | Topic | Status |
|---|---|---|
| 1–2 | Kickoff, basics | planned |
| 3 | Start: app, Docker, CI | planned |
| 4 | Kubernetes, CD | planned |
| 5 | Terraform, Helm, cache, E2E | planned |
| 6 | GitOps | planned |

## Layout

```
app/     Python app and tests
k8s/     Kubernetes manifests
infra/   Terraform
docs/    Architecture notes and diagrams
```

## License

MIT
