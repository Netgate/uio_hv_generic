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
for POSTINST in %{_prefix}/lib/dkms/common.postinst %{_datarootdir}/%{name}/postinst; do
        if [ -f $POSTINST ]; then
                $POSTINST %{name} %{version} %{_datarootdir}/%{name}
                exit $?
        fi
        echo "WARNING: $POSTINST does not exist."
done
echo -e "ERROR: DKMS version is too old and %{name} was not"
echo -e "built with legacy DKMS support."
echo -e "You must either rebuild %{name} with legacy postinst"
echo -e "support or upgrade DKMS to a more current version."
exit 1

%preun
echo -e
echo -e "Uninstall of %{name} module (version %{version}) beginning:"
dkms remove -m %{name} -v %{version} --all --rpm_safe_upgrade
exit 0
