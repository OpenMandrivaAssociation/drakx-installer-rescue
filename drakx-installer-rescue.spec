%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	family	drakx-installer
Summary:	Rescue image
Name:		%{family}-rescue
Version:	1.27
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2
Group:		Development/Other
Url:		https://wiki.mandriva.com/Tools/DrakX
BuildRequires:	perl-XML-Parser squashfs-tools mknod-m600
BuildRequires:	ldetect-lst-devel
BuildRequires:	hexedit grub rsync openssh-clients ncftp kbd strace
BuildRequires:	gpart parted partimage e2fsprogs
BuildRequires:	dump xfsdump eject testdisk extipl
BuildRequires:	xfsprogs reiserfsprogs jfsutils ntfsprogs dosfstools btrfs-progs
BuildRequires:	mdadm lvm2 dmraid kpartx dmraid-events dmsetup
BuildRequires:	setserial tcpdump
BuildRequires:	mt-st
Buildrequires:	krb5-appl-clients
Buildrequires:	db52-utils
BuildRequires:	pciutils ldetect
BuildRequires:	packdrake rpmtools
BuildRequires:	vim-minimal
BuildRequires:	drakx-installer-binaries drakxtools-backend drakx-kbd-mouse-x11
BuildRequires:	bind-utils nfs-utils-clients wget
BuildRequires:	ka-deploy-source-node
BuildRequires:	cdialog
BuildRequires:	ldetect-lst >= 0.1.222
BuildRequires:	ntfs-3g
BuildRequires:	cryptsetup photorec quota
BuildRequires:	pv
Buildrequires:	fakeroot 
BuildRequires:	uclibc-dropbear screen
BuildRequires:	nilfs-utils
# having issues moving this package in repos, so just workaround it for now..
#BuildRequires:	linux_logo
Patch0:		drakx-installer-rescue-1.27-workaround-bs-issues-with-linux_logo.patch

%description
rescue image

%prep
%setup -q
%patch0 -p0

%build
%make -C rescue

%install
%makeinstall_std -C rescue

%files
%dir %{_libdir}/%{family}
%dir %{_libdir}/%{family}/root
%dir %{_libdir}/%{family}/root/install
%dir %{_libdir}/%{family}/root/install/stage2/
%{_libdir}/%{family}/root/install/stage2/rescue.sqfs
