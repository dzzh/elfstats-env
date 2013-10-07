%define		ENVNAME elfstats
Name:		elfstats-env
Version:	1.0.2
Release:	1.el6
Summary:	A Python virtual environment configured to support elfstats. Requires Python 2.6.x/2.7.x to be installed in a system.

Group:		System Environment/Base
License:	MIT
URL:		https://github.com/dzzh/elfstats-env
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Prefix: 	/srv/virtualenvs
Requires:	/usr/bin/python
BuildRequires:	prelink

%description
This Python virtual environment is configured to support installation of elfstatsd and elfstats-munin.

%prep
%setup -q

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix}
cp -rp elfstats %{buildroot}%{prefix}

%install
# undo prelinking
/usr/sbin/prelink -u $RPM_BUILD_ROOT%{prefix}/%{ENVNAME}/bin/python

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{prefix}
%{prefix}/

%changelog

