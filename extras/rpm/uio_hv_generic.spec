%{!?_topdir: %define _topdir %(pwd)}

Name: uio_hv_generic
Version: %{_version}
Release: %{_release}
Summary: uio_hv_generic kernel module
Group: System Environment/Libraries
License: GPLv2
URL: https://netgate.com
Requires: dkms kernel-devel
ExclusiveArch: x86_64
Source0: %{name}-%{version}-%{release}.tar.xz

%description
Newer uio_hv_generic kernel module to run on Azure

%prep
%setup -q

%build

echo "Nothing to build..."

%install

%{__mkdir_p} %{buildroot}/%{_sysconfdir}/modules-load.d
echo %{name} > %{buildroot}/%{_sysconfdir}/modules-load.d/%{name}-modules.conf
%{__mkdir_p} %{buildroot}/usr/src/%{name}-%{version}
%{__install} -m 0644 src/* %{buildroot}/usr/src/%{name}-%{version}/

%files
/usr/src/*
%{_sysconfdir}/modules-load.d/*

%post

if [ $1 -gt 1 ]; then
	echo "Upgrading: module should already be present"
else
	dkms add -m %{name} -v %{version} --rpm_safe_upgrade
	dkms build -m %{name} -v %{version} --rpm_safe_upgrade
	dkms install -m %{name} -v %{version} --rpm_safe_upgrade
fi

%preun

if [ $1 -gt 0 ]; then
	echo "Upgrading: module should stay installed"
else
	dkms remove -m %{name} -v %{version} --all --rpm_safe_upgrade
fi
