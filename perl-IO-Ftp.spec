%define realname	IO-Ftp

Name:		perl-%{realname}
Version:	0.05
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Wrapper for Net::FTP
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel perl-URI

BuildArch:	noarch

%description
IO::Ftp is a wrapper for Net::FTP to simplify its use when
using its stor and retr methods.

%prep
%setup -q -n IO-Ftp-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

