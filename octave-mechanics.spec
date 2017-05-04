%define octpkg mechanics

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Functions for classical mechanics and structural analysis computations
Name:		octave-%{octpkg}
Version:	1.3.1
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-linear-algebra >= 2.0.0
Requires:	octave-general >= 1.2.2
Requires:	octave-geometry >= 1.2.1

Requires(post): octave
Requires(postun): octave

%description
Library with functions useful for numerical computation in classical
mechanics and structural analysis.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

