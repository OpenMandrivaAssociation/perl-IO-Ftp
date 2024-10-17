%define upstream_name	 IO-Ftp
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Wrapper for Net::FTP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-URI
BuildArch:	noarch

%description
IO::Ftp is a wrapper for Net::FTP to simplify its use when
using its stor and retr methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 655030
- rebuild for updated spec-helper

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 410065
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2009.0
+ Revision: 257312
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.05-4mdv2008.1
+ Revision: 151421
- rebuild for perl-5.10.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-3mdv2008.0
+ Revision: 86507
- rebuild


* Sat Aug 19 2006 Pascal Terjan <pterjan@mandriva.org> 0.05-2mdv2007.0
- BuildRequires perl-URI

* Fri Jun 16 2006 Pascal Terjan <pterjan@mandriva.org> 0.05-1mdv2007.0
- First Mandriva package

