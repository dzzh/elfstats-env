Name:		elfstats-env
Version:	1.0.1
Release:	1.el6
Summary:	A Python virtual environment configured to support elfstats. Requires Python 2.6.x/2.7.x to be installed in a system.

Group:		System Environment/Base
License:	MIT
URL:		https://github.com/dzzh/elfstats-env
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Prefix: 	/srv/virtualenvs

%description
This Python virtual environment is configured to support installation of elfstatsd and elfstats-munin.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix}
cp -rp elfstats %{buildroot}%{prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{prefix}
%{prefix}/

%changelog

