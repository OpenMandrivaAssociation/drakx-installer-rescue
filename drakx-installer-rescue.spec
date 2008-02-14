%define name drakx-installer-rescue
%define version 1.7
%define release %mkrel 3

%define ldetect_lst_version %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' ldetect-lst)

Summary: Rescue image
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-XML-Parser squashfs-tools mknod-m600
BuildRequires: ldetect-lst-devel
BuildRequires: hexedit grub telnet rsync openssh-clients ftp-client-krb5 kbd strace
BuildRequires: gpart parted partimage
BuildRequires: dump xfsdump eject testdisk extipl
BuildRequires: xfsprogs reiserfsprogs jfsprogs ntfsprogs dosfstools
BuildRequires: mdadm lvm2 dmraid
BuildRequires: setserial
BuildRequires: mt-st
BuildRequires: pciutils ldetect
BuildRequires: vim-minimal
BuildRequires: drakx-installer-binaries drakxtools-backend drakx-kbd-mouse-x11
BuildRequires: nfs-utils-clients
BuildRequires: ka-deploy-source-node

#- require the version used during build
Requires: ldetect-lst = %ldetect_lst_version

%description
rescue image

%prep
%setup -q

%build
make -C rescue

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
cp -r rescue/rescue.sqfs $dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name
