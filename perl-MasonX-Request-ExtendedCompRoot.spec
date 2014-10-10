%define upstream_name    MasonX-Request-ExtendedCompRoot
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Extend functionality of Mason's component root
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MasonX/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Mason)
BuildArch:	noarch

%description
"MasonX::Request::ExtendedCompRoot" lets you alter Mason's
component root during the lifetime of any given request or
subrequest. This behaviour is useful if you want to override
certain components, but cannot determine that at the moment you
create your handler (when you could in theory create an interp
object with a different component root) or because you configure
Mason in an httpd.conf.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/MasonX/Request/ExtendedCompRoot.pm
%{perl_vendorlib}/MasonX/Resolver/ExtendedCompRoot.pm
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-2mdv2010.0
+ Revision: 405862
- bump mkrel to force rebuild
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-4mdv2009.0
+ Revision: 241716
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix According to perl Policy
	- Source URL

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package

