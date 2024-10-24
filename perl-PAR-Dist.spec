%define modname	PAR-Dist

Summary:	Create and manipulate PAR distributions
Name:		perl-%{modname}
Version:	0.53
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/PAR::Dist
Source0:	http://www.cpan.org/modules/by-module/PAR/PAR-Dist-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-YAML-parser
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl-devel

%description
This module creates and manipulates *PAR distributions*. They are
architecture-specific PAR files, containing everything under blib/ of CPAN
distributions after their "make" or "Build" stage, a META.yml describing
metadata of the original CPAN distribution, and a MANIFEST detailing all files
within it. Digitally signed PAR distributions will also contain a SIGNATURE
file.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/PAR
%{_mandir}/man3/*


