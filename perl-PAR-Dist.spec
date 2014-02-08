%define upstream_name	 PAR-Dist
%define upstream_version 0.47

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Create and manipulate PAR distributions
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/PAR/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-YAML-parser
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/PAR


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-4mdv2012.0
+ Revision: 765585
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-3
+ Revision: 764095
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.470.0-2
+ Revision: 667285
- mass rebuild

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.470.0-1mdv2011.0
+ Revision: 472243
- update to 0.47

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.0
+ Revision: 410627
- update to 0.46

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.0
+ Revision: 407956
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2010.0
+ Revision: 387016
- update to new version 0.45

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2009.1
+ Revision: 337316
- update to new version 0.44

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2009.1
+ Revision: 333408
- update to new version 0.43

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2009.1
+ Revision: 324519
- update to new version 0.42

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdv2009.1
+ Revision: 320440
- update to new version 0.41

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2009.1
+ Revision: 297814
- update to new version 0.40

* Wed Oct 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2009.1
+ Revision: 296423
- update to new version 0.39

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 295515
- update to new version 0.38

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.1
+ Revision: 292341
- update to new version 0.37

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.31-2mdv2009.0
+ Revision: 268661
- rebuild early 2009.0 package (before pixel changes)

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.0
+ Revision: 212935
- update to new version 0.31

* Fri Feb 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2008.1
+ Revision: 164134
- update to new version 0.29

* Wed Feb 06 2008 Funda Wang <fwang@mandriva.org> 0.28-1mdv2008.1
+ Revision: 162942
- update to new version 0.28

* Tue Feb 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2008.1
+ Revision: 162589
- update to new version 0.27

* Mon Feb 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.1
+ Revision: 162065
- update to new version 0.26

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.25-1mdv2008.0
+ Revision: 59277
- 0.25

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2008.0
+ Revision: 55820
- update to new version 0.24

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2008.0
+ Revision: 46657
- update to new version 0.23


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.21-1mdv2007.0
+ Revision: 131695
- 0.21
- 0.18

* Tue Aug 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdv2007.0
+ Revision: 53972
- 0.15
- Import perl-PAR-Dist

* Sat Jun 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2007.0
- New version 0.10

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2007.0
- new version
- spec cleanup
- rpmbuildupate aware
- fix directory ownership

* Tue Feb 14 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.08-1mdk
- 0.08

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-3mdk
- rebuild; spec cleanup

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.07-2mdk
- rebuild for new perl

* Sat May 22 2004 Florin <florin@mandrakesoft.com> 0.07-1mdk
- first Mandrake Release

