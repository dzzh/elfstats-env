Name:		munin-plugins-environment		
Version:	1.0
Release:	1%{?dist}
Summary:	A Python virtual environment configured to support Munin monitoring plugins.

Group:		System Environment/Base
License:	TomTom proprietary
URL:		http://scm.tomtomgroup.com/munin-plugins/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
This Python virtual environment is configured to support installation of munindaemon and pymunin-tomtom.

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/virtualenvs
cp -rp munin %{buildroot}/srv/virtualenvs

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/srv/virtualenvs/munin/*



%changelog

