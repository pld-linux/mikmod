Summary:	XM, MOD, MTM, S3M, STM, ULT, IT and UNI module player
Summary(pl.UTF-8):	Odtwarzacz modułów dźwiękowych XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Summary(pt_BR.UTF-8):	Reprodutor de arquivos de som XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Summary(es.UTF-8):	Reproductor de archivos de sonido XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Name:		mikmod
Version:	3.2.8
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz
# Source0-md5:	01478623b273d7d2e2c6e45c1c478533
URL:		http://mikmod.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	libmikmod-devel >= 3.2.0
BuildRequires:	ncurses-devel >= 5.0
Requires:	libmikmod >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MikMod is one of the best and most well known MOD music file players
for UNIX-like systems. This particular distribution is intended to
compile fairly painlessly in a Linux environment. MikMod uses the OSS
/dev/dsp driver including all recent kernels for output, and will also
write .WAV files. Supported file formats include 669, AMF, APUN, DSM,
FAR, GDM, IT, IMF, MOD, MED, MTM, OKT, S3M, STM, STX, ULT, UNI and XM.
The player uses ncurses for console output and supports transparent
loading from gzip/pkzip/zoo archives and the loading/saving of
playlists.

%description -l pl.UTF-8
MikMod jest odtwarzaczem modułów dla systemów uniksowych, w tym dla
Linuksa. Potrafi odtwarzać poprzez OSS (/dev/dsp) oraz zapisywać do
plików .WAV. Obsługującym formaty modułów to: 669, AMF, APUN, DSM,
FAR, GDM, IT, IMF, MOD, MED, MTM, OKT, S3M, STM, STX, ULT, UNI i XM.
Odtwarzacz ma tekstowy interfejs ncurses, potrafi w sposób
przezroczysty wczytywać moduły z archiwów gzip/pkzip/zoo; obsługuje
także playlisty (odczyt i zapis).

%description -l pt_BR.UTF-8
Um dos melhores e mais conhecido reprodutor de MOD para Unix. Reproduz
músicas em formato MOD.

O MikMod é um reprodutor portável de módulos originalmente escrito por
Jean-Paul Mikkers (MikMak) para o DOS. Ele foi subseqüentemente
modificado por muitas mãos e agora roda em muitas plataformas, com
esta distribuição projetada para compilar sem problemas em um ambiente
Unix (Linux). Ele usa o driver /dev/dsp OSS incluso em todos os kernel
recentes para saída e também escreve arquivos WAV. Os formatos de
arquivos suportados incluem: mod, stm, s3m, mtm, xm e it. O reprodutor
usa ncurses para saída no console e suporta carga transparente de
arquivos gzip/pkzip/zoo e carga/gravação de listas de músicas para
reprodução.

%description -l es.UTF-8
Uno de los mejores y más conocido reproductor de MOD para Unix.
Reproduce músicas en formato MOD. MikMod es un reproductor portátil de
módulos originalmente escrito por Jean-Paul Mikkers (MikMak) para el
DOS. Fue sucesivamente modificado por muchas manos y ahora se ejecuta
en muchas plataformas, con esta distribución proyectada para compilar
sin problemas en un ambiente Unix (Linux). Usa el driver /dev/dsp OSS
incluso en todos los kernel recientes para salida y también escribe
archivos WAV. Los formatos de archivos soportados incluyen: mod, stm,
s3m, mtm, xm y it. El reproductor usa ncurses para salida en la
pantalla y soporta carga transparente de archivos gzip/pkzip/zoo y
carga/grabación de listas de músicas para reproducción.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mikmod
%{_datadir}/mikmod
%{_mandir}/man1/mikmod.1*
