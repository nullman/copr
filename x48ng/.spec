Name:           x48ng
Version:        1.3.0
Release:        1%{?dist}
Summary:        HP 48 emulator
License:        GPL2
URL:            https://github.com/nullman/copr/x48ng/
Source0:        https://github.com/nullman/copr/blob/97ae2fdbf33e4c9e8497b0d682b08ef16eda1377/x48ng/1.3.0.tar.gz
BuildRequires:  lua-devel, readline-devel, SDL3-devel
Requires:

%description
Fork of x48-0.6.4.

%prep
%setup -q -n x48ng-%{version}

%build
make get-roms
make

%install
sudo make install PREFIX=/usr

%files
%{buildroot}/usr/bin/x48ng
%{buildroot}/usr/bin/x48ng-launcher
%{buildroot}/usr/share/x48ng/
%{buildroot}/usr/share/doc/x48ng/
%{buildroot}/usr/share/applications/x48ng.desktop
%{buildroot}/usr/share/man/man1/x48ng.1

%docs
AUTHORS LICENSE README.md

%changelog
Author: Gwenhael Le Moine <gwenhael.le.moine@gmail.com>
Date:   Tue Jul 7 16:34:54 2026 +0200

    1.3.0
