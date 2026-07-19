Name:           x48ng
Version:        1.3.0
Release:        1%{?dist}
Summary:        HP 48 emulator
License:        GPL-2.0-or-later
URL:            https://github.com/nullman/copr/x48ng/
Source0:        https://github.com/nullman/copr/archive/refs/tags/copr-1.0.1.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua-devel
BuildRequires:  readline-devel
BuildRequires:  SDL3-devel

%description
x48ng is a modern fork of the x48 HP-48SX/GX emulator.

%prep
%autosetup -n x48ng-%{version}

%build
%make_build

%install
%make_install

%files
%{_bindir}/x48ng
%{_bindir}/x48ng-launcher
%{_datadir}/x48ng
%{_docdir}/x48ng
%{_datadir}/applications/x48ng.desktop
%{_mandir}/man1/x48ng.1.gz

%changelog
* Tue Jul 7 2026 Gwenhael Le Moine <gwenhael.le.moine@gmail.com> - 1.3.0-1
  - Initial release
