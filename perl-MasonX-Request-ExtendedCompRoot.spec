%define realname MasonX-Request-ExtendedCompRoot

Summary:	MasonX::Request::ExtendedCompRoot - Extend  functionality of Mason's component root
Name:           perl-%{realname}
Version:        0.03
Release:        %mkrel 4
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MasonX/%{realname}-%{version}.tar.bz2 
BuildRequires:	perl-HTML-Mason >= 1.24
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
"MasonX::Request::ExtendedCompRoot" lets you alter Mason's
component root during the lifetime of any given request or
subrequest. This behaviour is useful if you want to override
certain components, but cannot determine that at the moment you
create your handler (when you could in theory create an interp
object with a different component root) or because you configure
Mason in an httpd.conf.

%prep

%setup -q -n %{realname}-%{version}

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

