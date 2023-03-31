Name:		texlive-milog
Version:	41610
Release:	2
Summary:	A LaTeX class for fulfilling the documentation duties according to the German minimum wage law MiLoG
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/milog
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/milog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/milog.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Seit dem 1. Januar 2015 gilt in Deutschland grundsatzlich fur
alle Arbeitnehmer ein flachendeckender gesetzlicher Mindestlohn
in Hohe von derzeit 8,50EUR pro Stunde. Mit Wirkung ab 1.
August 2015 wurden die Dokumentations- und
Aufzeichnungspflichten gelockert. Nach SS17 MiLoG, muss Beginn,
Ende und Dauer der taglichen Arbeitszeit der in SS22 MiLoG
definierten Arbeitnehmern (formlos) aufgezeichnet werden.
Zusatzlich ermoglicht milog.cls aus praktischen Grunden die
Aufzeichnug von unbezahlten Pausen und Bemerkungen (Ruhetag,
Urlaub, krank, ...). Die Erfassung der Arbeitszeiten erfolgt in
einer simplen CSV-Datei, aus der die Klasse automatisch einen
Arbeitszeitnachweis erstellt. Alternativ konnen die Daten auch
durch einen CSV-Export - mit eventueller Nachbearbeitung -
einer geeigneteten App erhoben werden. The milog.cls class
provides means to fulfill the documentation duties by the
German minimum wage law MiLoG. The recording of working hours
is carried out in a simple CSV file from which the class will
automatically create a time sheet. Alternatively, data can also
be collected by a CSV export of a suitable app.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/milog
%doc %{_texmfdistdir}/doc/latex/milog

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
