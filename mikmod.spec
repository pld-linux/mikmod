Summary:	Sound module player
Name:		mikmod
Version:	3.0.4
Release:	1
Copyright:	GPL/LGPL
Vendor:		Miodrag Vallat <miodrag@mygale.org>
URL:		http://www.mygale.org/~miodrag/mikmod/index.html
Group:		Applications/Sound
Source:		http://www.mygale.org/~miodrag/mikmod/%{name}-%{version}.tar.gz
Patch0:		mikmod-s3mvolslides.patch
Patch1:		mikmod-config.patch
Patch2:		mikmod-ncurses.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
mikmod is a 669, DSM, FAR, IT, MOD, MED, MTM, S3M,
ULT, XM, and MOD-15 player.  This version built with
OSS, ncurses, and CPU time snagger support.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -s mikmod $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README README.EsounD README.SGI README.SUN AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.EsounD,README.SGI,README.SUN,AUTHORS,ChangeLog}.gz
%attr(755, root, root) %{_bindir}/mikmod

%changelog
* Fri Jul 09 1999 Jan Rêkorajski <baggins@pld.org.pl>
- FHS 2.0
- gzipping docs
- macros

* Fri Sep 25 1998 Joel Young <jyoung@erols.com>
- created RPM spec file
