Name:		munin-plugins-environment		
Version:	1.01
Release:	1.el6
Summary:	A Python virtual environment configured to support Munin monitoring plugins.

Group:		System Environment/Base
License:	TomTom Proprietary
URL:		http://scm.tomtomgroup.com/munin-plugins/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  x86_64
Prefix: 	/srv/virtualenvs

%description
This Python virtual environment is configured to support installation of munindaemon and pymunin-tomtom.
http://vos.intra.local/display/SS3/Monitoring+Apache+performance+at+Community+servers+with+Munin

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix}
cp -rp munin %{buildroot}%{prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{prefix}
%{prefix}/

%changelog

