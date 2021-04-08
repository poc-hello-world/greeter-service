# Greeter Service

[![GitHub License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://opensource.org/licenses/MIT)
[![Gitpod: ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod&style=flat-square)](https://gitpod.io/from-referrer/)

[![Mergify Status](https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/poc-hello-world/greeter-service&style=flat-square)](https://mergify.io)
[![Maintenance status: best-effort](https://img.shields.io/badge/Maintained%3F-best--effort-yellow?style=flat-square)](https://github.com/vlaaaaaaad)

Proof-of-Concept (PoC) application that returns a greeting. It is indented to be called by another application that composes a "_Greeting name!_" output.

For example for "_Hello world!_" this app would be the one providing the "_Hello_".

![Architecture diagram](./assets/poc-hello-world.png)

## Intended use

The purpose of this application is to be used for microservices tech demos and example implementations of tools.

**It is in no way, shape, or form a reference for best practices, a good example, or a comprehensive anything**. It is a minimal skeleton app with simple logic that can easily be extended.

For more complex demos see:

- Google Cloud Platform's [microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo)
- Microsoft's [eShopOnContainers](https://github.com/dotnet-architecture/eShopOnContainers)
- Weaveworks' and Container Solutions' [Sock Shop](https://github.com/microservices-demo/microservices-demo)
- Istio's [BookInfo](https://istio.io/docs/examples/bookinfo/)
- Kubernetes' [Guestbook](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/)

## Configuration and forking

This repository is fork-friendly!

- fork this repository
- go to the "_Actions_" tab and enable GitHub Actions
- setup relevant secrets
  - to build and push a container image to Amazon ECR
    - `AWS_ACCESS_KEY_ID` looking something like `AKIAIOSFODNN7EXAMPLE`
    - `AWS_SECRET_ACCESS_KEY` looking something like `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
- change relevant values in `.github/workflows/app-build-and-push.yaml`
- change something in the code and create a new Pull Request

## Forks

If you extend this application to do something, please create a Pull Request back with a link to your fork.

| Fork link | Extras added                              |
| --------- | ----------------------------------------- |
|           | + dynamically read greeting from DynamoDB |

## License

This project is provided under the [MIT License](https://opensource.org/licenses/MIT). See [LICENSE](./LICENSE) for more information.
