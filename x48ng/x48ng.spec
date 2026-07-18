Name:           x48ng
Version:        1.3.0
Release:        1%{?dist}
Summary:        HP 48 emulator
License:        GPL-2.0-or-later
URL:            https://github.com/nullman/copr/%{name}
Source0:        https://github.com/nullman/copr/blob/%{name}-%{version}/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)

%description
x48ng is a modern fork of the x48 HP-48SX/GX emulator.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-launcher
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Jul 7 2026 Gwenhael Le Moine <gwenhael.le.moine@gmail.com> - 1.3.0-1
  - Initial release
