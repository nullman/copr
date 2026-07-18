Name:           galendae
Version:        0
Release:        1%{?dist}
Summary:        Lightweight popup calendar
License:        MIT
URL:            https://github.com/chris-marsh/galendae
Source0:        https://github.com/chris-marsh/galendae/archive/refs/heads/master.tar.gz
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       gtk3

%description
A lightweight popup calendar that can be styled to match workspace themes.

%prep
%autosetup -n galendae-master

%build
%make_build release

%install
install -Dpm0755 galendae %{buildroot}%{_bindir}/galendae
install -d %{buildroot}%{_datadir}/galendae/config
install -pm0644 config/* %{buildroot}%{_datadir}/galendae/config/
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license LICENSE
%{_bindir}/galendae
%{_datadir}/galendae/

%changelog
* Sun Aug 30 2026 Chris Marsh <chris.pm@gmail.com> - 0-1
  - Initial Fedora package
