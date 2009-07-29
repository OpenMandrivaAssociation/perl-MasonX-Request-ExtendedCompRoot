%define upstream_name    MasonX-Request-ExtendedCompRoot
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	MasonX::Request::ExtendedCompRoot - Extend  functionality of Mason's component root
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MasonX/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildRequires:	perl-HTML-Mason >= 1.24
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%{__make}

%check
%__make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/MasonX/Request/ExtendedCompRoot.pm
%{perl_vendorlib}/MasonX/Resolver/ExtendedCompRoot.pm
%{_mandir}/man3/*
