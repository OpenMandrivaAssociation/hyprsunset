Name:		hyprsunset
Version:	0.1.0
Release:	1
Summary:	An application to enable a blue-light filter on Hyprland
Group:		Hyprland
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprsunset
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(hyprutils)>=0.2.3
BuildRequires:	pkgconfig(hyprwayland-scanner)>=0.4.0
BuildRequires:	pkgconfig(hyprland-protocols)>=0.4.0

BuildSystem: cmake

%description
%{summary}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
