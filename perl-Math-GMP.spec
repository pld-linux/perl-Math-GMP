#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	GMP
Summary:	Math::GMP Perl module - High speed arbitrary size integer math
Summary(pl):	Modu³ Perla Math::GMP - szybka arytmetyka liczb ca³kowitych o dowolnym rozmiarze
Name:		perl-Math-GMP
Version:	2.03
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	gmp-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::GMP gives you access to the fast GMP library for fast big
integer math.

%description -l pl
Math::GMP daje dostêp do szybkiej biblioteki GMP dla szybkich
obliczeñ na du¿ych liczbach ca³kowitych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_sitearch}/Math/GMP.pm
%dir %{perl_sitearch}/auto/Math/GMP
%{perl_sitearch}/auto/Math/GMP/GMP.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/GMP/GMP.so
%{perl_sitearch}/auto/Math/GMP/autosplit.ix
%{_mandir}/man3/*
