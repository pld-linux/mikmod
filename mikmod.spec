%define		ver	3.1.6
%define		rel	a
Summary:	Sound module player
Summary(pl):	Odtwarzacz modu³ów d¼wiêkowych
Name:		mikmod
Version:	%{ver}%{rel}
Release:	3
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://mikmod.darkorb.net/mikmod/%{name}-%{ver}.tar.gz
Patch0:		mikmod-%{ver}-a.patch
URL:		http://mikmod.darkorb.net/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libmikmod-devel >= 3.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mikmod is a 669, DSM, FAR, IT, MOD, MED, MTM, S3M, ULT, XM, and MOD-15
player.

%description -l pl
mikmod jest odtwarzaczem modu³ów obs³uguj±cym formaty: 669, DSM, FAR,
IT, MOD, MED, MTM, S3M, ULT, XM i MOD-15.

%prep
%setup -q -n %{name}-%{ver}
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
LDFLAGS="-s";
export CFLAGS LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,NEWS}.gz
%attr(755,root,root) %{_bindir}/mikmod

%{_mandir}/man1/*
