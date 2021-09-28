%global debug_package %{nil}

Name:		 puppet_agent_exporter
Version: 1.0.0
Release: el6
Summary: Prometheus puppet agent exporter
License: MIT
URL:     https://github.com/monitoring-tools/prom-puppet-agent-exporter
Conflicts: puppet_agent_exporter

Source0: puppet_agent_exporter.init
Source1: puppet_agent_exporter.default

%description

Prometheus exporter for nginx logs


%build
/bin/true

%install
install -D -m 755 puppet_agent_exporter %{buildroot}%{_bindir}/puppet_agent_exporter
install -D -m 755 %{SOURCE0} %{buildroot}%{_initrddir}/puppet_agent_exporter
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/default/puppet_agent_exporter

%files
%defattr(-,root,root,-)
%{_bindir}/puppet_agent_exporter
%{_initrddir}/puppet_agent_exporter
%{_sysconfdir}/default/puppet_agent_exporter