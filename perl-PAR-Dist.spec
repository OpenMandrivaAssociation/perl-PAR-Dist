%define modname	PAR-Dist
%define modver 0.51

Summary:	Create and manipulate PAR distributions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/PAR::Dist
Source0:	http://www.cpan.org/modules/by-module/PAR/PAR-Dist-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/PAR
%{_mandir}/man3/*


