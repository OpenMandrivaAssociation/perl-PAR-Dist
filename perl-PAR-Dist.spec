%define upstream_name	 PAR-Dist
%define upstream_version 0.47

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Create and manipulate PAR distributions
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/PAR/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-YAML-parser
BuildRequires:	perl(Archive::Zip)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module creates and manipulates *PAR distributions*. They are
architecture-specific PAR files, containing everything under blib/ of CPAN
distributions after their "make" or "Build" stage, a META.yml describing
metadata of the original CPAN distribution, and a MANIFEST detailing all files
within it. Digitally signed PAR distributions will also contain a SIGNATURE
file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
