Summary:        Rescue image
Name:           drakx-installer-rescue
Version:        1.22
Release:        2
Source0:        %{name}-%{version}.tar.bz2
License:        GPL
Group:          Development/Other
Url:            http://wiki.mandriva.com/Tools/DrakX
BuildRequires:  perl-XML-Parser squashfs-tools mknod-m600
BuildRequires:  ldetect-lst-devel
BuildRequires:  hexedit grub rsync openssh-clients ncftp kbd strace
BuildRequires:  gpart parted partimage e2fsprogs
BuildRequires:  dump xfsdump eject testdisk extipl
BuildRequires:  xfsprogs reiserfsprogs jfsutils ntfsprogs dosfstools btrfs-progs
BuildRequires:  mdadm lvm2 dmraid kpartx dmraid-events dmsetup
BuildRequires:  setserial tcpdump
BuildRequires:  mt-st
Buildrequires:  krb5-appl-clients
Buildrequires:  db52-utils
BuildRequires:  pciutils ldetect
BuildRequires:  packdrake rpmtools
BuildRequires:  vim-minimal
BuildRequires:  drakx-installer-binaries drakxtools-backend drakx-kbd-mouse-x11
BuildRequires:  bind-utils nfs-utils-clients wget
BuildRequires:  ka-deploy-source-node
BuildRequires:  cdialog
BuildRequires:  ldetect-lst >= 0.1.222
BuildRequires:  ntfs-3g
BuildRequires:  cryptsetup photorec quota
BuildRequires:  pv
Buildrequires:  fakeroot 
BuildRequires:  dropbear screen gdisk

%description
rescue image

%prep
%setup -q

%build
make -C rescue

%install
dest=%{buildroot}%{_libdir}/%{name}
mkdir -p $dest
cp -r rescue/rescue.sqfs $dest

%files
%{_libdir}/%{name}
