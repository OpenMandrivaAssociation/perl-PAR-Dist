%define module	PAR-Dist
%define name	perl-%{module}
%define version 0.25
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Create and manipulate PAR distributions
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/PAR/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
This module creates and manipulates *PAR distributions*. They are
architecture-specific PAR files, containing everything under blib/ of CPAN
distributions after their "make" or "Build" stage, a META.yml describing
metadata of the original CPAN distribution, and a MANIFEST detailing all files
within it. Digitally signed PAR distributions will also contain a SIGNATURE
file.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/PAR



