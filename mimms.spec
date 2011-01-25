%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: MMS stream downloader
Name: mimms
Version: 3.2.1
Release: 6%{?dist}
License: GPLv3+
Group: Applications/Multimedia
URL: http://savannah.nongnu.org/projects/mimms/
Source: http://download.savannah.gnu.org/releases/mimms/mimms-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
Requires: libmms >= 0.4
BuildArch: noarch

%description
mimms is a program designed to allow you to download streams using the MMS
protocol and save them to your computer, as opposed to watching them live.


%prep
%setup -q


%build
# No configure or SMP, this is just some python code
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/mimms
%{python_sitelib}/mimms-*.egg-info
%{python_sitelib}/libmimms/
%{_mandir}/man1/mimms.1*


%changelog
* Tue Jan 25 2011 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.2.1-6
- rebuilt

* Mon Jan 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.2.1-5
- Rebuilt for python

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 3.2.1-4
- rebuild for new F11 features

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 3.2.1-3
- Rebuild for new python.

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 3.2.1-2
- rebuild for RPM Fusion

* Sun Mar 18 2008 Matthias Saou <http://freshrpms.net/> 3.2.1-1
- Initial RPM release.

