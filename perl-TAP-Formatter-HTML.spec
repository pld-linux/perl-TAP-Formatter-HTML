#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	TAP
%define		pnam	Formatter-HTML
%include	/usr/lib/rpm/macros.perl
Summary:	TAP::Formatter::HTML - TAP Test Harness output delegate for HTML output
Summary(pl.UTF-8):	TAP::Formatter::HTML - moduł TAP Test Harness tworzący wyjście HTML
Name:		perl-TAP-Formatter-HTML
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/TAP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	897821d527c67c52dfd6df89b70ceec6
URL:		http://search.cpan.org/dist/TAP-Formatter-HTML/
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Temp >= 0.17
BuildRequires:	perl-Template-Toolkit >= 2.14
BuildRequires:	perl-Template-Toolkit-Plugin-Date >= 2.14
BuildRequires:	perl-Test-Harness >= 3.17
BuildRequires:	perl-Test-Simple >= 0.01
BuildRequires:	perl-URI >= 1.35
BuildRequires:	perl-accessors >= 0.02
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides HTML output formatting for TAP::Harness (a
replacement for Test::Harness. It is largely based on ideas from
TAP::Test::HTMLMatrix (which was built on Test::Harness and thus had a
few limitations - hence this module).

%description -l pl.UTF-8
Ten moduł zapewnia formatowanie wyjścia HTML dla TAP::Harness
(zamiennika Test::Harness). Jest w dużej części oparty na ideach
TAP::Test::HTMLMatrix (który został stworzony w oparciu o
Test::Harness, przez co miał kilka ograniczeń - dlatego powstał ten
moduł).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Todo
# NOTE: move dir to perl-dirs if another plugin appears
%dir %{perl_vendorlib}/App/Prove/Plugin
%{perl_vendorlib}/App/Prove/Plugin/HTML.pm
%{perl_vendorlib}/TAP/Formatter/HTML.pm
%{perl_vendorlib}/TAP/Formatter/HTML
%{_mandir}/man3/App::Prove::Plugin::HTML.3pm*
%{_mandir}/man3/TAP::Formatter::HTML*.3pm*
%{_examplesdir}/%{name}-%{version}
