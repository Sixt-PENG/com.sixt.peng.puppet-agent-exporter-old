%global debug_package %{nil}

Name:		 puppet_agent_exporter
Version: 1.0.0
Release: el7
Summary: Prometheus puppet agent exporter
License: MIT
URL:     https://github.com/monitoring-tools/prom-puppet-agent-exporter
Conflicts: puppet_agent_exporter

Source0: puppet_agent_exporter.service
Source1: puppet_agent_exporter.default

%{?systemd_requires}
Requires(pre): shadow-utils

%description

Prometheus exporter for puppet agent

%build
/bin/true

%install
install -D -m 755 puppet_agent_exporter %{buildroot}%{_bindir}/puppet_agent_exporter
install -D -m 644 %{SOURCE0} %{buildroot}%{_unitdir}/puppet_agent_exporter.service
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/default/puppet_agent_exporter

%post
%systemd_post puppet_agent_exporter.service

%preun
%systemd_preun puppet_agent_exporter.service

%postun
%systemd_postun puppet_agent_exporter.service

%files
%defattr(-,root,root,-)
%{_bindir}/puppet_agent_exporter
%{_unitdir}/puppet_agent_exporter.service
%{_sysconfdir}/default/puppet_agent_exporter