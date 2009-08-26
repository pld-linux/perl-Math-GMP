#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	GMP
Summary:	Math::GMP Perl module - high speed arbitrary size integer math
Summary(pl.UTF-8):	Moduł Perla Math::GMP - szybka arytmetyka liczb całkowitych o dowolnym rozmiarze
Name:		perl-Math-GMP
Version:	2.05
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d719578064fb935e2f8403ba0340179a
URL:		http://search.cpan.org/dist/Math-GMP/
BuildRequires:	gmp-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::GMP gives you access to the fast GMP library for fast big
integer math.

%description -l pl.UTF-8
Math::GMP daje dostęp do szybkiej biblioteki GMP dla szybkich
obliczeń na dużych liczbach całkowitych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%ifarch %{x8664} alpha ia64 ppc64 s390x sparc64
# original reference values expect 32-bit long
%{__perl} -pi -e 's/^\+9999999999(9*):[0-9]+$/+9999999999$1:9999999999$1/' t/gmppm.t
%endif

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_vendorarch}/Math/GMP.pm
%dir %{perl_vendorarch}/auto/Math/GMP
%{perl_vendorarch}/auto/Math/GMP/GMP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/GMP/GMP.so
%{perl_vendorarch}/auto/Math/GMP/autosplit.ix
%{_mandir}/man3/*
