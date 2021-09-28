# Puppet Agent Exporter

`Puppet Agent Exporter` is puppet agent report statistics exporter for Prometheus. It has been adapted to work with the go build command (instead of using a Makefile) as well as unnecessary files have been removed.

The `Puppet Agent Exporter` reads last run summary report and exposes them for Prometheus consumption.

## Building and running

The application can be easily built using the following command:

```
go build
```

### RPM Build/Spec for Prometheus-Katello Service Discovery and dependencies

Tries to follow the [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines) from Fedora.

* Binary: `/usr/bin/prometheus-katello-sd`

#### Build

The build happens using Docker.

- Just run ```docker-compose up --build --force-recreate```
- The rpm is finally created into the RPMS directory

### Configuration Flags

Name                    | Default                                     | Description
----------------------- | ------------------------------------------- | -----------
web.listen-address      | localhost:9001                              | Address on which to expose metrics and web interface.
web.telemetry-path      | /metrics                                    | Path under which to expose metrics.
namespace               | puppet                                      | The namespace of metrics.
puppet.last-run-summary | /var/lib/puppet/state/last_run_summary.yaml | Path to the puppet's last run summary report.
puppet.last-run-report  |                                             | Path to the puppet's last run full report - need only if you want to get info from full report.
puppet.disabled-lock    |                                             | Path to the puppet's agent disabled lock-file.

## What's exported?
It exports statistics from standard Puppet report (https://puppet.com/blog/puppet-monitoring-how-to-monitor-success-or-failure-of-puppet-runs).
