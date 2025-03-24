Name:		hyprsunset
Version:	0.2.0
Release:	1
Summary:	An application to enable a blue-light filter on Hyprland
Group:		Hyprland
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprsunset
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(hyprutils)
BuildRequires:	pkgconfig(hyprwayland-scanner)
BuildRequires:	pkgconfig(hyprland-protocols)

Recommends: pkgconfig(hyprland) >= 0.48.0

BuildSystem: cmake

%description
%{summary}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
