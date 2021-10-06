FROM centos:centos7
LABEL maintainer="Joseph Hofmann <joseph.hofmann@sixt.com>"

RUN yum update -y
RUN yum install -y rpmdevtools mock wget git

ADD * /root/rpmbuild/ROOT/
RUN cd /root && rpmdev-setuptree
ADD SOURCES/* /root/rpmbuild/SOURCES/
ADD SPECS/* /root/rpmbuild/SPECS/
RUN ln -s /root/rpmbuild/RPMS /RPMS
RUN wget -qO- https://golang.org/dl/go1.16.2.linux-amd64.tar.gz | tar xzf - -C /usr/share/
RUN echo "Go Version: $(/usr/share/go/bin/go version)"
RUN echo "Building: $(cd /root/rpmbuild/ROOT && /usr/share/go/bin/go build -o /root/rpmbuild/BUILD/puppet_agent_exporter)"

VOLUME ["/RPMS"]

WORKDIR /root

RUN rm -rf /RPMS/* || true

CMD set -x && spectool -g -R rpmbuild/SPECS/puppet_agent_exporter_el6.spec && rpmbuild -ba rpmbuild/SPECS/puppet_agent_exporter_el6.spec